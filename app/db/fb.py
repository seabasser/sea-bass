from firebase import firebase


class Firebase(object):

    def __init__(self):
        self.fb = firebase.FirebaseApplication("https://cbaas-eac89-default-rtdb.firebaseio.com/", None)

