import random
import json
import urllib
import web

class JsonService:

    def _to2DecimalPlaces(self, price):
        return '%.2f' % price
        
    def _getPriceDifferenceDescription(self, priceDiff):
        if priceDiff < 0.0:
            return   self._to2DecimalPlaces(abs(priceDiff)) + " cheaper at Argos"
        elif priceDiff > 0.0: 
            return  self._to2DecimalPlaces(abs(priceDiff)) + " more expensive at Argos"
        else:
            return "The same price"

    def _getCompetitorsPrice(self, argosPrice):
        priceAsFloat = float(argosPrice)
        argosPricePlus20Percent = priceAsFloat * 1.2
        argosPriceMinus20Percent = priceAsFloat*  0.8
        competitorsPrice = random.uniform(argosPriceMinus20Percent, argosPricePlus20Percent)
        priceAsStr =  self._to2DecimalPlaces(competitorsPrice)
        return priceAsStr
        
    def _addCompetitorsPriceToJson(self, jsonData):
            for deal in jsonData:
                competitorsPrice = self._getCompetitorsPrice(deal["price"])
                deal["competitorsPrice"] = competitorsPrice

    def _getArgosJsonData(self):
        url = "http://api.hotukdeals.com/rest_api/v2/?key=d8c3d15dd702b7b19e037dce8bfe28ff&order=hot&output=json&results_per_page=10&merchant=argos&exclude_expired=true"
        response = urllib.urlopen(url)
        jsonData = json.loads(response.read())
        return jsonData
        
    def _getPriceDifference(self, deal):
        argosPrice = float(deal["price"])
        compPrice = float(deal["competitorsPrice"])        
        return argosPrice - compPrice
        
    def _sortDealsByPriceDifference(self, dealsList):
        sortedList = sorted(dealsList, key = lambda deal : self._getPriceDifference(deal))
        return sortedList
        
    def _getHottestArgosDeals(self, rawJsonData):
        return rawJsonData["deals"]["items"]
        
    def _addPriceDifferenceInformationToJson(self, dealsJsonList):
        for deal in dealsJsonList:
            priceDifference = self._getPriceDifference(deal)
            priceDifferenceDescription = self._getPriceDifferenceDescription(priceDifference)
            deal["priceDifferenceDescription"] = priceDifferenceDescription
            
    def _getDealId(self, imageUrl):
            lastSlash = imageUrl.rfind("/")
            dot = imageUrl.rfind(".")
            dealId = imageUrl[lastSlash + 1:dot]
            return dealId
            
    def _addArgosSiteURL(self, dealsList):
        for deal in dealsList:
            imageUrl = deal["deal_image"]
            dealId = self._getDealId(imageUrl)
            argosUrl = "http://www.hotukdeals.com/visit?m=5&q=" + dealId
            deal["argosUrl"] = argosUrl

    def GET(self):
        argosJsonData = self._getArgosJsonData()
        hottestArgosDeals = self._getHottestArgosDeals(argosJsonData)
        self._addCompetitorsPriceToJson(hottestArgosDeals)
        self._addPriceDifferenceInformationToJson(hottestArgosDeals)
        self._addArgosSiteURL(hottestArgosDeals)
        dealsSortedByPriceDifference = self._sortDealsByPriceDifference(hottestArgosDeals)
        web.header('Content-Type', 'application/json')
        return json.dumps(dealsSortedByPriceDifference)