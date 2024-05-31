from creator.py import WebSite, MobileApp, ManagerCall

def main():
    website = WebSite()
    mobile_app = MobileApp()
    manager_call = ManagerCall()

    domestic_sub = website.create_subscription("domestic")
    educational_sub = mobile_app.create_subscription("educational")
    premium_sub = manager_call.create_subscription("premium")

    print(domestic_sub)
    print(educational_sub)
    print(premium_sub)

if __name__ == "__main__":
    main()
