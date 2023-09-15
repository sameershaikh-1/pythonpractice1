#ENG 3 >> Place an order

# class ordersmethod:
#
#     def orders_upstox(self):

#         print("order placed successfully")

from login_1 import loginmethod
lg = loginmethod()     # creating object
lg.login_upstox()


from watchlist import watchlistmethod

wl = watchlistmethod()
wl.watchlist_upstox()

from orders import ordersmethod

or1 = ordersmethod()
or1.orders_upstox()