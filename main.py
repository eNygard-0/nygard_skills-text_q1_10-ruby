from js import document

def create_order(e=None):
    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")
    item6 = document.getElementById("item6")
    item7 = document.getElementById("item7")
    item8 = document.getElementById("item8")
    
    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked + 
             float(item4.value) * item4.checked + 
             float(item5.value) * item5.checked +
             float(item6.value) * item6.checked +
             float(item7.value) * item7.checked +
             float(item8.value) * item8.checked)
    
    customer_name = document.getElementById("customer").value
    customer_address = document.getElementById("address").value
    contact_number = document.getElementById("contact_number").value
    
    document.getElementById("order_output1").innerText = f"Order for: {customer_name}"
    document.getElementById("order_output2").innerText = f"Address: {customer_address}"
    document.getElementById("order_output3").innerText = f"Contact number: {contact_number}"
    document.getElementById("show").innerText = f"Total: $ {total:.2f}"
