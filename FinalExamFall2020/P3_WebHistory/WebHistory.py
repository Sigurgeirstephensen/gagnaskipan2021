class dll_node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class WebHistory:
    # You can change this to be one sentinel node if you are more comfortable with that type of solution
    def __init__(self):
        self.home_page = "ru.is"
        self.head = dll_node("head sentinel, this string is for debugging and should not be printed")
        self.tail = dll_node("tail sentinel, this string is for debugging and should not be printed")
        self.curr_page = dll_node(self.home_page, self.head, self.tail)
        self.head.next = self.curr_page
        self.tail.prev = self.curr_page


    def nav_to_website(self, web_url):
        new_node = dll_node(web_url,self.curr_page,self.tail)
        new_node.prev.next = new_node
        self.tail.prev = new_node
        self.curr_page = new_node

    def press_back(self):
        pass

    def press_forward(self):
        pass

    #calling print on this object calls this function, printing the 
    #dll from start to front and adds "><" around the curr_page
    def __str__(self):
        ret_str = ""
        temp_node = self.head.next
        while temp_node != self.tail:
            if temp_node == self.curr_page:
                ret_str += ">" + temp_node.value + "< "
            else:
                ret_str += temp_node.value + " "
            temp_node = temp_node.next
        return ret_str

if __name__ == "__main__":
    w = WebHistory()
    print(w)
    w.nav_to_website("google.com")
    print(w)
    w.nav_to_website("wikipedia.com")
    print(w)
    w.nav_to_website("ruv.is")
    print(w)
    w.nav_to_website("reddit.com")
    print(w)
    w.press_back()
    print(w)
    w.press_back()
    print(w)
    w.press_back()
    print(w)
    w.nav_to_website("visir.is")
    print(w)
    w.press_forward()
    print(w)
    w.press_back()
    print(w)

        
