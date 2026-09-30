Set app=createobject("arena.application")

app.visible=true

Set Model=app.models.add()
Model.ActiveView.AutoConnect = False
Model.ActiveView.SmartConnections = True

Dim xValues(1)
Dim yValues(1)


xValues(0)=0
xValues(1)=0

yValues(0)=0
yValues(1)=0

Set Create1=Model.Modules.Create("BasicProcess","Create",1400,700)
Create1.Data("Name")="Create1"
Set Process_Create_Purchase_Requisition=Model.Modules.Create("BasicProcess","Process",2600,700)
Process_Create_Purchase_Requisition.Data("Name")="Create Purchase Requisition"
Set Process_Analyze_Purchase_Requisition=Model.Modules.Create("BasicProcess","Process",3800,700)
Process_Analyze_Purchase_Requisition.Data("Name")="Analyze Purchase Requisition"
Set Decide1=Model.Modules.Create("BasicProcess","Decide",5000,700)
Decide1.Data("Name")="Decide1"
Set Process_Amend_Purchase_Requisition=Model.Modules.Create("BasicProcess","Process",6200,700)
Process_Amend_Purchase_Requisition.Data("Name")="Amend Purchase Requisition"
Set Process_Create_Request_for_Quotation=Model.Modules.Create("BasicProcess","Process",1400,1500)
Process_Create_Request_for_Quotation.Data("Name")="Create Request for Quotation"
Set Process_Analyze_Request_for_Quotation=Model.Modules.Create("BasicProcess","Process",2600,1500)
Process_Analyze_Request_for_Quotation.Data("Name")="Analyze Request for Quotation"
Set Decide2=Model.Modules.Create("BasicProcess","Decide",3800,1500)
Decide2.Data("Name")="Decide2"
Set Process_Amend_Request_for_Quotation=Model.Modules.Create("BasicProcess","Process",5000,1500)
Process_Amend_Request_for_Quotation.Data("Name")="Amend Request for Quotation"
Set Process_Send_Request_for_Quotation_to_Supplier=Model.Modules.Create("BasicProcess","Process",6200,1500)
Process_Send_Request_for_Quotation_to_Supplier.Data("Name")="Send Request for Quotation to Supplier"
Set Process_Create_Quotation_comparison_Map=Model.Modules.Create("BasicProcess","Process",1400,2300)
Process_Create_Quotation_comparison_Map.Data("Name")="Create Quotation comparison Map"
Set Process_Analyze_Quotation_Comparison_Map=Model.Modules.Create("BasicProcess","Process",2600,2300)
Process_Analyze_Quotation_Comparison_Map.Data("Name")="Analyze Quotation Comparison Map"
Set Process_Choose_best_option=Model.Modules.Create("BasicProcess","Process",3800,2300)
Process_Choose_best_option.Data("Name")="Choose best option"
Set Process_Settle_Conditions_With_Supplier=Model.Modules.Create("BasicProcess","Process",5000,2300)
Process_Settle_Conditions_With_Supplier.Data("Name")="Settle Conditions With Supplier"
Set Process_Create_Purchase_Order=Model.Modules.Create("BasicProcess","Process",6200,2300)
Process_Create_Purchase_Order.Data("Name")="Create Purchase Order"
Set Process_Confirm_Purchase_Order=Model.Modules.Create("BasicProcess","Process",1400,3100)
Process_Confirm_Purchase_Order.Data("Name")="Confirm Purchase Order"
Set Process_Deliver_Goods_Services=Model.Modules.Create("BasicProcess","Process",2600,3100)
Process_Deliver_Goods_Services.Data("Name")="Deliver Goods Services"
Set Process_Release_Purchase_Order=Model.Modules.Create("BasicProcess","Process",3800,3100)
Process_Release_Purchase_Order.Data("Name")="Release Purchase Order"
Set Process_Approve_Purchase_Order_for_payment=Model.Modules.Create("BasicProcess","Process",5000,3100)
Process_Approve_Purchase_Order_for_payment.Data("Name")="Approve Purchase Order for payment"
Set Process_Send_Invoice=Model.Modules.Create("BasicProcess","Process",6200,3100)
Process_Send_Invoice.Data("Name")="Send Invoice"
Set Process_Release_Suppliers_Invoice=Model.Modules.Create("BasicProcess","Process",1400,3900)
Process_Release_Suppliers_Invoice.Data("Name")="Release Suppliers Invoice"
Set Decide3=Model.Modules.Create("BasicProcess","Decide",2600,3900)
Decide3.Data("Name")="Decide3"
Set Process_Settle_Dispute_With_Supplier=Model.Modules.Create("BasicProcess","Process",3800,3900)
Process_Settle_Dispute_With_Supplier.Data("Name")="Settle Dispute With Supplier"
Set Process_Authorize_Suppliers_Invoice_payment=Model.Modules.Create("BasicProcess","Process",5000,3900)
Process_Authorize_Suppliers_Invoice_payment.Data("Name")="Authorize Suppliers Invoice payment"
Set Process_Pay_Invoice=Model.Modules.Create("BasicProcess","Process",6200,3900)
Process_Pay_Invoice.Data("Name")="Pay Invoice"
Set Dispose1=Model.Modules.Create("BasicProcess","Dispose",1400,4700)
Dispose1.Data("Name")="Dispose1"

Model.Connections.Create _
Create1.Shape, _
Process_Create_Purchase_Requisition.Shape


Model.Connections.Create _
Process_Create_Purchase_Requisition.Shape, _
Process_Analyze_Purchase_Requisition.Shape


Model.Connections.Create _
Process_Approve_Purchase_Order_for_payment.Shape, _
Process_Send_Invoice.Shape


Model.Connections.Create _
Process_Settle_Conditions_With_Supplier.Shape, _
Process_Create_Purchase_Order.Shape


Model.Connections.Create _
Process_Amend_Purchase_Requisition.Shape, _
Process_Analyze_Purchase_Requisition.Shape


Model.Connections.Create _
Process_Create_Request_for_Quotation.Shape, _
Process_Analyze_Request_for_Quotation.Shape


Model.Connections.Create _
Process_Send_Invoice.Shape, _
Process_Release_Suppliers_Invoice.Shape


Model.Connections.Create _
Process_Analyze_Purchase_Requisition.Shape, _
Decide1.Shape


Model.Connections.Create _
Process_Analyze_Request_for_Quotation.Shape, _
Decide2.Shape


Model.Connections.Create _
Process_Amend_Request_for_Quotation.Shape, _
Process_Analyze_Request_for_Quotation.Shape


Model.Connections.Create _
Process_Pay_Invoice.Shape, _
Dispose1.Shape


Model.Connections.Create _
Process_Analyze_Quotation_Comparison_Map.Shape, _
Process_Choose_best_option.Shape


Model.Connections.Create _
Process_Release_Suppliers_Invoice.Shape, _
Decide3.Shape


Model.Connections.Create _
Process_Authorize_Suppliers_Invoice_payment.Shape, _
Process_Pay_Invoice.Shape


Model.Connections.Create _
Process_Create_Purchase_Order.Shape, _
Process_Confirm_Purchase_Order.Shape


Model.Connections.Create _
Process_Deliver_Goods_Services.Shape, _
Process_Release_Purchase_Order.Shape


Model.Connections.Create _
Process_Settle_Dispute_With_Supplier.Shape, _
Process_Authorize_Suppliers_Invoice_payment.Shape


Model.Connections.Create _
Process_Release_Purchase_Order.Shape, _
Process_Approve_Purchase_Order_for_payment.Shape


Model.Connections.Create _
Process_Confirm_Purchase_Order.Shape, _
Process_Deliver_Goods_Services.Shape


Model.Connections.Create _
Process_Create_Quotation_comparison_Map.Shape, _
Process_Analyze_Quotation_Comparison_Map.Shape


Model.Connections.Create _
Process_Send_Request_for_Quotation_to_Supplier.Shape, _
Process_Create_Quotation_comparison_Map.Shape


Model.Connections.Create _
Process_Choose_best_option.Shape, _
Process_Settle_Conditions_With_Supplier.Shape


Model.Connections.Create _
Decide3.Shape, _
Process_Settle_Dispute_With_Supplier.Shape, _
"Next Label No"


Model.Connections.Create _
Decide3.Shape, _
Process_Authorize_Suppliers_Invoice_payment.Shape, _
"Next Label Yes"


Model.Connections.Create _
Decide2.Shape, _
Process_Amend_Request_for_Quotation.Shape, _
"Next Label No"


Model.Connections.Create _
Decide2.Shape, _
Process_Send_Request_for_Quotation_to_Supplier.Shape, _
"Next Label Yes"


Model.Connections.Create _
Decide1.Shape, _
Process_Amend_Purchase_Requisition.Shape, _
"Next Label No"


Model.Connections.Create _
Decide1.Shape, _
Process_Create_Request_for_Quotation.Shape, _
"Next Label Yes"


