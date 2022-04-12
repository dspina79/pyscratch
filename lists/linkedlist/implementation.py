import linkedelementmod  as ll

x = ll.ListElement(10)
x.setItem(ll.ListElement(20))
y = ll.ListElement(30)
y.setItem(x.next_item)
x.setItem(y)
x.printList()