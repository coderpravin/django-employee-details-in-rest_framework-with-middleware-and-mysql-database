#function based middlewares

def MyEmployeeMiddleware(get_response):
    print("Intially Run the code")

    def myfunction(request):
        print("Before the hit the view show me display")
        response = get_response(request)
        print("After the hit the view show me display1")
        return response
    return myfunction
