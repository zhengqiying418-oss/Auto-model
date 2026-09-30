
On Error Resume Next
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

Set Res_Alberto_Duport=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Alberto_Duport.Data("Name")="Alberto Duport"
Res_Alberto_Duport.Data("Capacity")="1"
Set Res_Anna_Kaufmann=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Anna_Kaufmann.Data("Name")="Anna Kaufmann"
Res_Anna_Kaufmann.Data("Capacity")="1"
Set Res_Anne_Olwada=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Anne_Olwada.Data("Name")="Anne Olwada"
Res_Anne_Olwada.Data("Capacity")="1"
Set Res_Carmen_Finacse=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Carmen_Finacse.Data("Name")="Carmen Finacse"
Res_Carmen_Finacse.Data("Capacity")="1"
Set Res_Christian_Francois=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Christian_Francois.Data("Name")="Christian Francois"
Res_Christian_Francois.Data("Capacity")="1"
Set Res_Clement_Duchot=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Clement_Duchot.Data("Name")="Clement Duchot"
Res_Clement_Duchot.Data("Capacity")="1"
Set Res_Elvira_Lores=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Elvira_Lores.Data("Name")="Elvira Lores"
Res_Elvira_Lores.Data("Capacity")="1"
Set Res_Esmana_Liubiata=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Esmana_Liubiata.Data("Name")="Esmana Liubiata"
Res_Esmana_Liubiata.Data("Capacity")="1"
Set Res_Esmeralda_Clay=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Esmeralda_Clay.Data("Name")="Esmeralda Clay"
Res_Esmeralda_Clay.Data("Capacity")="1"
Set Res_Fjodor_Kowalski=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Fjodor_Kowalski.Data("Name")="Fjodor Kowalski"
Res_Fjodor_Kowalski.Data("Capacity")="1"
Set Res_Francis_Odell=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Francis_Odell.Data("Name")="Francis Odell"
Res_Francis_Odell.Data("Capacity")="1"
Set Res_Francois_de_Perrier=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Francois_de_Perrier.Data("Name")="Francois de Perrier"
Res_Francois_de_Perrier.Data("Capacity")="1"
Set Res_Heinz_Gutschmidt=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Heinz_Gutschmidt.Data("Name")="Heinz Gutschmidt"
Res_Heinz_Gutschmidt.Data("Capacity")="1"
Set Res_Immanuel_Karagianni=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Immanuel_Karagianni.Data("Name")="Immanuel Karagianni"
Res_Immanuel_Karagianni.Data("Capacity")="1"
Set Res_Karalda_Nimwada=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Karalda_Nimwada.Data("Name")="Karalda Nimwada"
Res_Karalda_Nimwada.Data("Capacity")="1"
Set Res_Karel_de_Groot=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Karel_de_Groot.Data("Name")="Karel de Groot"
Res_Karel_de_Groot.Data("Capacity")="1"
Set Res_Karen_Clarens=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Karen_Clarens.Data("Name")="Karen Clarens"
Res_Karen_Clarens.Data("Capacity")="1"
Set Res_Kim_Passa=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Kim_Passa.Data("Name")="Kim Passa"
Res_Kim_Passa.Data("Capacity")="1"
Set Res_Kiu_Kan=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Kiu_Kan.Data("Name")="Kiu Kan"
Res_Kiu_Kan.Data("Capacity")="1"
Set Res_Magdalena_Predutta=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Magdalena_Predutta.Data("Name")="Magdalena Predutta"
Res_Magdalena_Predutta.Data("Capacity")="1"
Set Res_Maris_Freeman=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Maris_Freeman.Data("Name")="Maris Freeman"
Res_Maris_Freeman.Data("Capacity")="1"
Set Res_Miu_Hanwan=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Miu_Hanwan.Data("Name")="Miu Hanwan"
Res_Miu_Hanwan.Data("Capacity")="1"
Set Res_Nico_Ojenbeer=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Nico_Ojenbeer.Data("Name")="Nico Ojenbeer"
Res_Nico_Ojenbeer.Data("Capacity")="1"
Set Res_Pedro_Alvares=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Pedro_Alvares.Data("Name")="Pedro Alvares"
Res_Pedro_Alvares.Data("Capacity")="1"
Set Res_Penn_Osterwalder=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Penn_Osterwalder.Data("Name")="Penn Osterwalder"
Res_Penn_Osterwalder.Data("Capacity")="1"
Set Res_Sean_Manney=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Sean_Manney.Data("Name")="Sean Manney"
Res_Sean_Manney.Data("Capacity")="1"
Set Res_Tesca_Lobes=Model.Modules.Create("BasicProcess","Resource",0,0)
Res_Tesca_Lobes.Data("Name")="Tesca Lobes"
Res_Tesca_Lobes.Data("Capacity")="1"
Set Set_Create_Request_for_Quotation=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Create_Request_for_Quotation.Data("Name")="Set_Create_Request_for_Quotation"
Set_Create_Request_for_Quotation.Data("Resource Name(1)")="Kim Passa"
Set_Create_Request_for_Quotation.Data("Resource Name(2)")="Immanuel Karagianni"
Set_Create_Request_for_Quotation.Data("Resource Name(3)")="Clement Duchot"
Set_Create_Request_for_Quotation.Data("Resource Name(4)")="Heinz Gutschmidt"
Set_Create_Request_for_Quotation.Data("Resource Name(5)")="Miu Hanwan"
Set_Create_Request_for_Quotation.Data("Resource Name(6)")="Nico Ojenbeer"
Set_Create_Request_for_Quotation.Data("Resource Name(7)")="Maris Freeman"
Set_Create_Request_for_Quotation.Data("Resource Name(8)")="Anna Kaufmann"
Set_Create_Request_for_Quotation.Data("Resource Name(9)")="Tesca Lobes"
Set_Create_Request_for_Quotation.Data("Resource Name(10)")="Francis Odell"
Set_Create_Request_for_Quotation.Data("Resource Name(11)")="Penn Osterwalder"
Set_Create_Request_for_Quotation.Data("Resource Name(12)")="Fjodor Kowalski"
Set_Create_Request_for_Quotation.Data("Resource Name(13)")="Anne Olwada"
Set_Create_Request_for_Quotation.Data("Resource Name(14)")="Esmana Liubiata"
Set_Create_Request_for_Quotation.Data("Resource Name(15)")="Christian Francois"
Set_Create_Request_for_Quotation.Data("Resource Name(16)")="Alberto Duport"
Set_Create_Request_for_Quotation.Data("Resource Name(17)")="Elvira Lores"
Set Set_Create_Purchase_Requisition=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Create_Purchase_Requisition.Data("Name")="Set_Create_Purchase_Requisition"
Set_Create_Purchase_Requisition.Data("Resource Name(1)")="Kim Passa"
Set_Create_Purchase_Requisition.Data("Resource Name(2)")="Esmana Liubiata"
Set_Create_Purchase_Requisition.Data("Resource Name(3)")="Tesca Lobes"
Set_Create_Purchase_Requisition.Data("Resource Name(4)")="Fjodor Kowalski"
Set_Create_Purchase_Requisition.Data("Resource Name(5)")="Christian Francois"
Set_Create_Purchase_Requisition.Data("Resource Name(6)")="Anne Olwada"
Set_Create_Purchase_Requisition.Data("Resource Name(7)")="Alberto Duport"
Set_Create_Purchase_Requisition.Data("Resource Name(8)")="Penn Osterwalder"
Set_Create_Purchase_Requisition.Data("Resource Name(9)")="Immanuel Karagianni"
Set_Create_Purchase_Requisition.Data("Resource Name(10)")="Clement Duchot"
Set_Create_Purchase_Requisition.Data("Resource Name(11)")="Elvira Lores"
Set_Create_Purchase_Requisition.Data("Resource Name(12)")="Nico Ojenbeer"
Set_Create_Purchase_Requisition.Data("Resource Name(13)")="Anna Kaufmann"
Set_Create_Purchase_Requisition.Data("Resource Name(14)")="Miu Hanwan"
Set Set_Create_Purchase_Order=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Create_Purchase_Order.Data("Name")="Set_Create_Purchase_Order"
Set_Create_Purchase_Order.Data("Resource Name(1)")="Karel de Groot"
Set_Create_Purchase_Order.Data("Resource Name(2)")="Magdalena Predutta"
Set_Create_Purchase_Order.Data("Resource Name(3)")="Francois de Perrier"
Set Set_Send_Request_for_Quotation_to_Supplier=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Send_Request_for_Quotation_to_Supplier.Data("Name")="Set_Send_Request_for_Quotation_to_Supplier"
Set_Send_Request_for_Quotation_to_Supplier.Data("Resource Name(1)")="Karel de Groot"
Set_Send_Request_for_Quotation_to_Supplier.Data("Resource Name(2)")="Magdalena Predutta"
Set_Send_Request_for_Quotation_to_Supplier.Data("Resource Name(3)")="Francois de Perrier"
Set Set_Approve_Purchase_Order_for_payment=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Approve_Purchase_Order_for_payment.Data("Name")="Set_Approve_Purchase_Order_for_payment"
Set_Approve_Purchase_Order_for_payment.Data("Resource Name(1)")="Karel de Groot"
Set_Approve_Purchase_Order_for_payment.Data("Resource Name(2)")="Magdalena Predutta"
Set_Approve_Purchase_Order_for_payment.Data("Resource Name(3)")="Francois de Perrier"
Set Set_Analyze_Request_for_Quotation=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Analyze_Request_for_Quotation.Data("Name")="Set_Analyze_Request_for_Quotation"
Set_Analyze_Request_for_Quotation.Data("Resource Name(1)")="Karel de Groot"
Set_Analyze_Request_for_Quotation.Data("Resource Name(2)")="Francois de Perrier"
Set_Analyze_Request_for_Quotation.Data("Resource Name(3)")="Magdalena Predutta"
Set Set_Pay_Invoice=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Pay_Invoice.Data("Name")="Set_Pay_Invoice"
Set_Pay_Invoice.Data("Resource Name(1)")="Pedro Alvares"
Set_Pay_Invoice.Data("Resource Name(2)")="Karalda Nimwada"
Set Set_Create_Quotation_comparison_Map=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Create_Quotation_comparison_Map.Data("Name")="Set_Create_Quotation_comparison_Map"
Set_Create_Quotation_comparison_Map.Data("Resource Name(1)")="Magdalena Predutta"
Set_Create_Quotation_comparison_Map.Data("Resource Name(2)")="Karel de Groot"
Set_Create_Quotation_comparison_Map.Data("Resource Name(3)")="Francois de Perrier"
Set Set_Settle_Conditions_With_Supplier=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Settle_Conditions_With_Supplier.Data("Name")="Set_Settle_Conditions_With_Supplier"
Set_Settle_Conditions_With_Supplier.Data("Resource Name(1)")="Francois de Perrier"
Set_Settle_Conditions_With_Supplier.Data("Resource Name(2)")="Karel de Groot"
Set_Settle_Conditions_With_Supplier.Data("Resource Name(3)")="Magdalena Predutta"
Set Set_Choose_best_option=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Choose_best_option.Data("Name")="Set_Choose_best_option"
Set_Choose_best_option.Data("Resource Name(1)")="Tesca Lobes"
Set_Choose_best_option.Data("Resource Name(2)")="Nico Ojenbeer"
Set_Choose_best_option.Data("Resource Name(3)")="Esmana Liubiata"
Set_Choose_best_option.Data("Resource Name(4)")="Alberto Duport"
Set_Choose_best_option.Data("Resource Name(5)")="Christian Francois"
Set_Choose_best_option.Data("Resource Name(6)")="Anne Olwada"
Set_Choose_best_option.Data("Resource Name(7)")="Penn Osterwalder"
Set_Choose_best_option.Data("Resource Name(8)")="Elvira Lores"
Set_Choose_best_option.Data("Resource Name(9)")="Clement Duchot"
Set_Choose_best_option.Data("Resource Name(10)")="Miu Hanwan"
Set_Choose_best_option.Data("Resource Name(11)")="Kim Passa"
Set_Choose_best_option.Data("Resource Name(12)")="Fjodor Kowalski"
Set_Choose_best_option.Data("Resource Name(13)")="Immanuel Karagianni"
Set_Choose_best_option.Data("Resource Name(14)")="Anna Kaufmann"
Set Set_Release_Suppliers_Invoice=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Release_Suppliers_Invoice.Data("Name")="Set_Release_Suppliers_Invoice"
Set_Release_Suppliers_Invoice.Data("Resource Name(1)")="Karalda Nimwada"
Set_Release_Suppliers_Invoice.Data("Resource Name(2)")="Pedro Alvares"
Set Set_Authorize_Suppliers_Invoice_payment=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Authorize_Suppliers_Invoice_payment.Data("Name")="Set_Authorize_Suppliers_Invoice_payment"
Set_Authorize_Suppliers_Invoice_payment.Data("Resource Name(1)")="Karalda Nimwada"
Set_Authorize_Suppliers_Invoice_payment.Data("Resource Name(2)")="Pedro Alvares"
Set Set_Analyze_Quotation_Comparison_Map=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Analyze_Quotation_Comparison_Map.Data("Name")="Set_Analyze_Quotation_Comparison_Map"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(1)")="Immanuel Karagianni"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(2)")="Anna Kaufmann"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(3)")="Fjodor Kowalski"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(4)")="Penn Osterwalder"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(5)")="Miu Hanwan"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(6)")="Clement Duchot"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(7)")="Christian Francois"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(8)")="Nico Ojenbeer"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(9)")="Esmana Liubiata"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(10)")="Anne Olwada"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(11)")="Tesca Lobes"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(12)")="Alberto Duport"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(13)")="Elvira Lores"
Set_Analyze_Quotation_Comparison_Map.Data("Resource Name(14)")="Kim Passa"
Set Set_Send_Invoice=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Send_Invoice.Data("Name")="Set_Send_Invoice"
Set_Send_Invoice.Data("Resource Name(1)")="Kiu Kan"
Set_Send_Invoice.Data("Resource Name(2)")="Karen Clarens"
Set_Send_Invoice.Data("Resource Name(3)")="Esmeralda Clay"
Set_Send_Invoice.Data("Resource Name(4)")="Sean Manney"
Set_Send_Invoice.Data("Resource Name(5)")="Carmen Finacse"
Set Set_Release_Purchase_Order=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Release_Purchase_Order.Data("Name")="Set_Release_Purchase_Order"
Set_Release_Purchase_Order.Data("Resource Name(1)")="Elvira Lores"
Set_Release_Purchase_Order.Data("Resource Name(2)")="Tesca Lobes"
Set_Release_Purchase_Order.Data("Resource Name(3)")="Nico Ojenbeer"
Set_Release_Purchase_Order.Data("Resource Name(4)")="Anne Olwada"
Set_Release_Purchase_Order.Data("Resource Name(5)")="Kim Passa"
Set_Release_Purchase_Order.Data("Resource Name(6)")="Miu Hanwan"
Set_Release_Purchase_Order.Data("Resource Name(7)")="Penn Osterwalder"
Set_Release_Purchase_Order.Data("Resource Name(8)")="Christian Francois"
Set_Release_Purchase_Order.Data("Resource Name(9)")="Alberto Duport"
Set_Release_Purchase_Order.Data("Resource Name(10)")="Clement Duchot"
Set_Release_Purchase_Order.Data("Resource Name(11)")="Immanuel Karagianni"
Set_Release_Purchase_Order.Data("Resource Name(12)")="Fjodor Kowalski"
Set_Release_Purchase_Order.Data("Resource Name(13)")="Esmana Liubiata"
Set_Release_Purchase_Order.Data("Resource Name(14)")="Anna Kaufmann"
Set Set_Deliver_Goods_Services=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Deliver_Goods_Services.Data("Name")="Set_Deliver_Goods_Services"
Set_Deliver_Goods_Services.Data("Resource Name(1)")="Sean Manney"
Set_Deliver_Goods_Services.Data("Resource Name(2)")="Kiu Kan"
Set_Deliver_Goods_Services.Data("Resource Name(3)")="Carmen Finacse"
Set_Deliver_Goods_Services.Data("Resource Name(4)")="Karen Clarens"
Set_Deliver_Goods_Services.Data("Resource Name(5)")="Esmeralda Clay"
Set Set_Confirm_Purchase_Order=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Confirm_Purchase_Order.Data("Name")="Set_Confirm_Purchase_Order"
Set_Confirm_Purchase_Order.Data("Resource Name(1)")="Sean Manney"
Set_Confirm_Purchase_Order.Data("Resource Name(2)")="Carmen Finacse"
Set_Confirm_Purchase_Order.Data("Resource Name(3)")="Kiu Kan"
Set_Confirm_Purchase_Order.Data("Resource Name(4)")="Karen Clarens"
Set_Confirm_Purchase_Order.Data("Resource Name(5)")="Esmeralda Clay"
Set Set_Settle_Dispute_With_Supplier=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Settle_Dispute_With_Supplier.Data("Name")="Set_Settle_Dispute_With_Supplier"
Set_Settle_Dispute_With_Supplier.Data("Resource Name(1)")="Karalda Nimwada"
Set_Settle_Dispute_With_Supplier.Data("Resource Name(2)")="Pedro Alvares"
Set_Settle_Dispute_With_Supplier.Data("Resource Name(3)")="Magdalena Predutta"
Set_Settle_Dispute_With_Supplier.Data("Resource Name(4)")="Karel de Groot"
Set_Settle_Dispute_With_Supplier.Data("Resource Name(5)")="Francois de Perrier"
Set Set_Analyze_Purchase_Requisition=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Analyze_Purchase_Requisition.Data("Name")="Set_Analyze_Purchase_Requisition"
Set_Analyze_Purchase_Requisition.Data("Resource Name(1)")="Heinz Gutschmidt"
Set_Analyze_Purchase_Requisition.Data("Resource Name(2)")="Maris Freeman"
Set_Analyze_Purchase_Requisition.Data("Resource Name(3)")="Francis Odell"
Set Set_Amend_Request_for_Quotation=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Amend_Request_for_Quotation.Data("Name")="Set_Amend_Request_for_Quotation"
Set_Amend_Request_for_Quotation.Data("Resource Name(1)")="Kim Passa"
Set_Amend_Request_for_Quotation.Data("Resource Name(2)")="Heinz Gutschmidt"
Set_Amend_Request_for_Quotation.Data("Resource Name(3)")="Anne Olwada"
Set_Amend_Request_for_Quotation.Data("Resource Name(4)")="Immanuel Karagianni"
Set_Amend_Request_for_Quotation.Data("Resource Name(5)")="Clement Duchot"
Set_Amend_Request_for_Quotation.Data("Resource Name(6)")="Nico Ojenbeer"
Set_Amend_Request_for_Quotation.Data("Resource Name(7)")="Fjodor Kowalski"
Set_Amend_Request_for_Quotation.Data("Resource Name(8)")="Esmana Liubiata"
Set_Amend_Request_for_Quotation.Data("Resource Name(9)")="Christian Francois"
Set_Amend_Request_for_Quotation.Data("Resource Name(10)")="Miu Hanwan"
Set_Amend_Request_for_Quotation.Data("Resource Name(11)")="Maris Freeman"
Set_Amend_Request_for_Quotation.Data("Resource Name(12)")="Anna Kaufmann"
Set_Amend_Request_for_Quotation.Data("Resource Name(13)")="Elvira Lores"
Set_Amend_Request_for_Quotation.Data("Resource Name(14)")="Tesca Lobes"
Set_Amend_Request_for_Quotation.Data("Resource Name(15)")="Penn Osterwalder"
Set_Amend_Request_for_Quotation.Data("Resource Name(16)")="Alberto Duport"
Set_Amend_Request_for_Quotation.Data("Resource Name(17)")="Francis Odell"
Set Set_Amend_Purchase_Requisition=Model.Modules.Create("BasicProcess","Set",0,0)
Set_Amend_Purchase_Requisition.Data("Name")="Set_Amend_Purchase_Requisition"
Set_Amend_Purchase_Requisition.Data("Resource Name(1)")="Kim Passa"
Set_Amend_Purchase_Requisition.Data("Resource Name(2)")="Penn Osterwalder"
Set_Amend_Purchase_Requisition.Data("Resource Name(3)")="Christian Francois"
Set_Amend_Purchase_Requisition.Data("Resource Name(4)")="Nico Ojenbeer"
Set_Amend_Purchase_Requisition.Data("Resource Name(5)")="Miu Hanwan"
Set_Amend_Purchase_Requisition.Data("Resource Name(6)")="Elvira Lores"
Set_Amend_Purchase_Requisition.Data("Resource Name(7)")="Immanuel Karagianni"
Set_Amend_Purchase_Requisition.Data("Resource Name(8)")="Clement Duchot"
Set Create1=Model.Modules.Create("BasicProcess","Create",1400,700)
Create1.Data("Name")="Create1"
Create1.Data("Interarrival Type")="Expression"
Create1.Data("Units")="Seconds"
Create1.Data("Expression")="EXPO(40672)"
Set Process_Create_Purchase_Requisition=Model.Modules.Create("BasicProcess","Process",2400,700)
Process_Create_Purchase_Requisition.Data("Name")="Create Purchase Requisition"
Process_Create_Purchase_Requisition.Data("Action")="Seize Delay Release"
Process_Create_Purchase_Requisition.Data("DelayType")="Expression"
Process_Create_Purchase_Requisition.Data("Units")="Seconds"
Process_Create_Purchase_Requisition.Data("Expression")="POIS(1843)"
Process_Create_Purchase_Requisition.Data("Resource Type(1)")="Set"
Process_Create_Purchase_Requisition.Data("Set Name(1)")="Set_Create_Purchase_Requisition"
Process_Create_Purchase_Requisition.Data("Quantity(1)")="1"
Process_Create_Purchase_Requisition.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Analyze_Purchase_Requisition=Model.Modules.Create("BasicProcess","Process",3400,700)
Process_Analyze_Purchase_Requisition.Data("Name")="Analyze Purchase Requisition"
Process_Analyze_Purchase_Requisition.Data("Action")="Seize Delay Release"
Process_Analyze_Purchase_Requisition.Data("DelayType")="Expression"
Process_Analyze_Purchase_Requisition.Data("Units")="Seconds"
Process_Analyze_Purchase_Requisition.Data("Expression")="UNIF(240,7500)"
Process_Analyze_Purchase_Requisition.Data("Resource Type(1)")="Set"
Process_Analyze_Purchase_Requisition.Data("Set Name(1)")="Set_Analyze_Purchase_Requisition"
Process_Analyze_Purchase_Requisition.Data("Quantity(1)")="1"
Process_Analyze_Purchase_Requisition.Data("Selection Rule(1)")="Smallest Number Busy"
Set Decide1=Model.Modules.Create("BasicProcess","Decide",4400,700)
Decide1.Data("Name")="Decide1"
Decide1.Data("Type")="2-way by Chance"
Decide1.Data("Percent True")="96.46"
Set Process_Amend_Purchase_Requisition=Model.Modules.Create("BasicProcess","Process",5400,700)
Process_Amend_Purchase_Requisition.Data("Name")="Amend Purchase Requisition"
Process_Amend_Purchase_Requisition.Data("Action")="Seize Delay Release"
Process_Amend_Purchase_Requisition.Data("DelayType")="Expression"
Process_Amend_Purchase_Requisition.Data("Units")="Seconds"
Process_Amend_Purchase_Requisition.Data("Expression")="POIS(1642)"
Process_Amend_Purchase_Requisition.Data("Resource Type(1)")="Set"
Process_Amend_Purchase_Requisition.Data("Set Name(1)")="Set_Amend_Purchase_Requisition"
Process_Amend_Purchase_Requisition.Data("Quantity(1)")="1"
Process_Amend_Purchase_Requisition.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Create_Request_for_Quotation=Model.Modules.Create("BasicProcess","Process",1400,1500)
Process_Create_Request_for_Quotation.Data("Name")="Create Request for Quotation"
Process_Create_Request_for_Quotation.Data("Action")="Seize Delay Release"
Process_Create_Request_for_Quotation.Data("DelayType")="Expression"
Process_Create_Request_for_Quotation.Data("Units")="Seconds"
Process_Create_Request_for_Quotation.Data("Expression")="UNIF(60,960)"
Process_Create_Request_for_Quotation.Data("Resource Type(1)")="Set"
Process_Create_Request_for_Quotation.Data("Set Name(1)")="Set_Create_Request_for_Quotation"
Process_Create_Request_for_Quotation.Data("Quantity(1)")="1"
Process_Create_Request_for_Quotation.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Analyze_Request_for_Quotation=Model.Modules.Create("BasicProcess","Process",2400,1500)
Process_Analyze_Request_for_Quotation.Data("Name")="Analyze Request for Quotation"
Process_Analyze_Request_for_Quotation.Data("Action")="Seize Delay Release"
Process_Analyze_Request_for_Quotation.Data("DelayType")="Expression"
Process_Analyze_Request_for_Quotation.Data("Units")="Seconds"
Process_Analyze_Request_for_Quotation.Data("Expression")="POIS(1382)"
Process_Analyze_Request_for_Quotation.Data("Resource Type(1)")="Set"
Process_Analyze_Request_for_Quotation.Data("Set Name(1)")="Set_Analyze_Request_for_Quotation"
Process_Analyze_Request_for_Quotation.Data("Quantity(1)")="1"
Process_Analyze_Request_for_Quotation.Data("Selection Rule(1)")="Smallest Number Busy"
Set Decide2=Model.Modules.Create("BasicProcess","Decide",3400,1500)
Decide2.Data("Name")="Decide2"
Decide2.Data("Type")="2-way by Chance"
Decide2.Data("Percent True")="48.6"
Set Process_Amend_Request_for_Quotation=Model.Modules.Create("BasicProcess","Process",4400,1500)
Process_Amend_Request_for_Quotation.Data("Name")="Amend Request for Quotation"
Process_Amend_Request_for_Quotation.Data("Action")="Seize Delay Release"
Process_Amend_Request_for_Quotation.Data("DelayType")="Expression"
Process_Amend_Request_for_Quotation.Data("Units")="Seconds"
Process_Amend_Request_for_Quotation.Data("Expression")="UNIF(300,1620)"
Process_Amend_Request_for_Quotation.Data("Resource Type(1)")="Set"
Process_Amend_Request_for_Quotation.Data("Set Name(1)")="Set_Amend_Request_for_Quotation"
Process_Amend_Request_for_Quotation.Data("Quantity(1)")="1"
Process_Amend_Request_for_Quotation.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Send_Request_for_Quotation_to_Supplier=Model.Modules.Create("BasicProcess","Process",5400,1500)
Process_Send_Request_for_Quotation_to_Supplier.Data("Name")="Send Request for Quotation to Supplier"
Process_Send_Request_for_Quotation_to_Supplier.Data("Action")="Seize Delay Release"
Process_Send_Request_for_Quotation_to_Supplier.Data("DelayType")="Expression"
Process_Send_Request_for_Quotation_to_Supplier.Data("Units")="Seconds"
Process_Send_Request_for_Quotation_to_Supplier.Data("Expression")="UNIF(60,8880)"
Process_Send_Request_for_Quotation_to_Supplier.Data("Resource Type(1)")="Set"
Process_Send_Request_for_Quotation_to_Supplier.Data("Set Name(1)")="Set_Send_Request_for_Quotation_to_Supplier"
Process_Send_Request_for_Quotation_to_Supplier.Data("Quantity(1)")="1"
Process_Send_Request_for_Quotation_to_Supplier.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Create_Quotation_comparison_Map=Model.Modules.Create("BasicProcess","Process",1400,2300)
Process_Create_Quotation_comparison_Map.Data("Name")="Create Quotation comparison Map"
Process_Create_Quotation_comparison_Map.Data("Action")="Seize Delay Release"
Process_Create_Quotation_comparison_Map.Data("DelayType")="Expression"
Process_Create_Quotation_comparison_Map.Data("Units")="Seconds"
Process_Create_Quotation_comparison_Map.Data("Expression")="POIS(12155)"
Process_Create_Quotation_comparison_Map.Data("Resource Type(1)")="Set"
Process_Create_Quotation_comparison_Map.Data("Set Name(1)")="Set_Create_Quotation_comparison_Map"
Process_Create_Quotation_comparison_Map.Data("Quantity(1)")="1"
Process_Create_Quotation_comparison_Map.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Analyze_Quotation_Comparison_Map=Model.Modules.Create("BasicProcess","Process",2400,2300)
Process_Analyze_Quotation_Comparison_Map.Data("Name")="Analyze Quotation Comparison Map"
Process_Analyze_Quotation_Comparison_Map.Data("Action")="Seize Delay Release"
Process_Analyze_Quotation_Comparison_Map.Data("DelayType")="Expression"
Process_Analyze_Quotation_Comparison_Map.Data("Units")="Seconds"
Process_Analyze_Quotation_Comparison_Map.Data("Expression")="POIS(1209)"
Process_Analyze_Quotation_Comparison_Map.Data("Resource Type(1)")="Set"
Process_Analyze_Quotation_Comparison_Map.Data("Set Name(1)")="Set_Analyze_Quotation_Comparison_Map"
Process_Analyze_Quotation_Comparison_Map.Data("Quantity(1)")="1"
Process_Analyze_Quotation_Comparison_Map.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Choose_best_option=Model.Modules.Create("BasicProcess","Process",3400,2300)
Process_Choose_best_option.Data("Name")="Choose best option"
Process_Choose_best_option.Data("Action")="Seize Delay Release"
Process_Choose_best_option.Data("DelayType")="Expression"
Process_Choose_best_option.Data("Units")="Seconds"
Process_Choose_best_option.Data("Expression")="0"
Process_Choose_best_option.Data("Resource Type(1)")="Set"
Process_Choose_best_option.Data("Set Name(1)")="Set_Choose_best_option"
Process_Choose_best_option.Data("Quantity(1)")="1"
Process_Choose_best_option.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Settle_Conditions_With_Supplier=Model.Modules.Create("BasicProcess","Process",4400,2300)
Process_Settle_Conditions_With_Supplier.Data("Name")="Settle Conditions With Supplier"
Process_Settle_Conditions_With_Supplier.Data("Action")="Seize Delay Release"
Process_Settle_Conditions_With_Supplier.Data("DelayType")="Expression"
Process_Settle_Conditions_With_Supplier.Data("Units")="Seconds"
Process_Settle_Conditions_With_Supplier.Data("Expression")="POIS(32389)"
Process_Settle_Conditions_With_Supplier.Data("Resource Type(1)")="Set"
Process_Settle_Conditions_With_Supplier.Data("Set Name(1)")="Set_Settle_Conditions_With_Supplier"
Process_Settle_Conditions_With_Supplier.Data("Quantity(1)")="1"
Process_Settle_Conditions_With_Supplier.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Create_Purchase_Order=Model.Modules.Create("BasicProcess","Process",5400,2300)
Process_Create_Purchase_Order.Data("Name")="Create Purchase Order"
Process_Create_Purchase_Order.Data("Action")="Seize Delay Release"
Process_Create_Purchase_Order.Data("DelayType")="Expression"
Process_Create_Purchase_Order.Data("Units")="Seconds"
Process_Create_Purchase_Order.Data("Expression")="POIS(573)"
Process_Create_Purchase_Order.Data("Resource Type(1)")="Set"
Process_Create_Purchase_Order.Data("Set Name(1)")="Set_Create_Purchase_Order"
Process_Create_Purchase_Order.Data("Quantity(1)")="1"
Process_Create_Purchase_Order.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Confirm_Purchase_Order=Model.Modules.Create("BasicProcess","Process",1400,3100)
Process_Confirm_Purchase_Order.Data("Name")="Confirm Purchase Order"
Process_Confirm_Purchase_Order.Data("Action")="Seize Delay Release"
Process_Confirm_Purchase_Order.Data("DelayType")="Expression"
Process_Confirm_Purchase_Order.Data("Units")="Seconds"
Process_Confirm_Purchase_Order.Data("Expression")="UNIF(240,9240)"
Process_Confirm_Purchase_Order.Data("Resource Type(1)")="Set"
Process_Confirm_Purchase_Order.Data("Set Name(1)")="Set_Confirm_Purchase_Order"
Process_Confirm_Purchase_Order.Data("Quantity(1)")="1"
Process_Confirm_Purchase_Order.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Deliver_Goods_Services=Model.Modules.Create("BasicProcess","Process",2400,3100)
Process_Deliver_Goods_Services.Data("Name")="Deliver Goods Services"
Process_Deliver_Goods_Services.Data("Action")="Seize Delay Release"
Process_Deliver_Goods_Services.Data("DelayType")="Expression"
Process_Deliver_Goods_Services.Data("Units")="Seconds"
Process_Deliver_Goods_Services.Data("Expression")="POIS(91075)"
Process_Deliver_Goods_Services.Data("Resource Type(1)")="Set"
Process_Deliver_Goods_Services.Data("Set Name(1)")="Set_Deliver_Goods_Services"
Process_Deliver_Goods_Services.Data("Quantity(1)")="1"
Process_Deliver_Goods_Services.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Release_Purchase_Order=Model.Modules.Create("BasicProcess","Process",3400,3100)
Process_Release_Purchase_Order.Data("Name")="Release Purchase Order"
Process_Release_Purchase_Order.Data("Action")="Seize Delay Release"
Process_Release_Purchase_Order.Data("DelayType")="Expression"
Process_Release_Purchase_Order.Data("Units")="Seconds"
Process_Release_Purchase_Order.Data("Expression")="60"
Process_Release_Purchase_Order.Data("Resource Type(1)")="Set"
Process_Release_Purchase_Order.Data("Set Name(1)")="Set_Release_Purchase_Order"
Process_Release_Purchase_Order.Data("Quantity(1)")="1"
Process_Release_Purchase_Order.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Approve_Purchase_Order_for_payment=Model.Modules.Create("BasicProcess","Process",4400,3100)
Process_Approve_Purchase_Order_for_payment.Data("Name")="Approve Purchase Order for payment"
Process_Approve_Purchase_Order_for_payment.Data("Action")="Seize Delay Release"
Process_Approve_Purchase_Order_for_payment.Data("DelayType")="Expression"
Process_Approve_Purchase_Order_for_payment.Data("Units")="Seconds"
Process_Approve_Purchase_Order_for_payment.Data("Expression")="60"
Process_Approve_Purchase_Order_for_payment.Data("Resource Type(1)")="Set"
Process_Approve_Purchase_Order_for_payment.Data("Set Name(1)")="Set_Approve_Purchase_Order_for_payment"
Process_Approve_Purchase_Order_for_payment.Data("Quantity(1)")="1"
Process_Approve_Purchase_Order_for_payment.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Send_Invoice=Model.Modules.Create("BasicProcess","Process",5400,3100)
Process_Send_Invoice.Data("Name")="Send Invoice"
Process_Send_Invoice.Data("Action")="Seize Delay Release"
Process_Send_Invoice.Data("DelayType")="Expression"
Process_Send_Invoice.Data("Units")="Seconds"
Process_Send_Invoice.Data("Expression")="0"
Process_Send_Invoice.Data("Resource Type(1)")="Set"
Process_Send_Invoice.Data("Set Name(1)")="Set_Send_Invoice"
Process_Send_Invoice.Data("Quantity(1)")="1"
Process_Send_Invoice.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Release_Suppliers_Invoice=Model.Modules.Create("BasicProcess","Process",1400,3900)
Process_Release_Suppliers_Invoice.Data("Name")="Release Suppliers Invoice"
Process_Release_Suppliers_Invoice.Data("Action")="Seize Delay Release"
Process_Release_Suppliers_Invoice.Data("DelayType")="Expression"
Process_Release_Suppliers_Invoice.Data("Units")="Seconds"
Process_Release_Suppliers_Invoice.Data("Expression")="POIS(269)"
Process_Release_Suppliers_Invoice.Data("Resource Type(1)")="Set"
Process_Release_Suppliers_Invoice.Data("Set Name(1)")="Set_Release_Suppliers_Invoice"
Process_Release_Suppliers_Invoice.Data("Quantity(1)")="1"
Process_Release_Suppliers_Invoice.Data("Selection Rule(1)")="Smallest Number Busy"
Set Decide3=Model.Modules.Create("BasicProcess","Decide",2400,3900)
Decide3.Data("Name")="Decide3"
Decide3.Data("Type")="2-way by Chance"
Decide3.Data("Percent True")="80.15"
Set Process_Settle_Dispute_With_Supplier=Model.Modules.Create("BasicProcess","Process",3400,3900)
Process_Settle_Dispute_With_Supplier.Data("Name")="Settle Dispute With Supplier"
Process_Settle_Dispute_With_Supplier.Data("Action")="Seize Delay Release"
Process_Settle_Dispute_With_Supplier.Data("DelayType")="Expression"
Process_Settle_Dispute_With_Supplier.Data("Units")="Seconds"
Process_Settle_Dispute_With_Supplier.Data("Expression")="UNIF(780,37200)"
Process_Settle_Dispute_With_Supplier.Data("Resource Type(1)")="Set"
Process_Settle_Dispute_With_Supplier.Data("Set Name(1)")="Set_Settle_Dispute_With_Supplier"
Process_Settle_Dispute_With_Supplier.Data("Quantity(1)")="1"
Process_Settle_Dispute_With_Supplier.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Authorize_Suppliers_Invoice_payment=Model.Modules.Create("BasicProcess","Process",4400,3900)
Process_Authorize_Suppliers_Invoice_payment.Data("Name")="Authorize Suppliers Invoice payment"
Process_Authorize_Suppliers_Invoice_payment.Data("Action")="Seize Delay Release"
Process_Authorize_Suppliers_Invoice_payment.Data("DelayType")="Expression"
Process_Authorize_Suppliers_Invoice_payment.Data("Units")="Seconds"
Process_Authorize_Suppliers_Invoice_payment.Data("Expression")="0"
Process_Authorize_Suppliers_Invoice_payment.Data("Resource Type(1)")="Set"
Process_Authorize_Suppliers_Invoice_payment.Data("Set Name(1)")="Set_Authorize_Suppliers_Invoice_payment"
Process_Authorize_Suppliers_Invoice_payment.Data("Quantity(1)")="1"
Process_Authorize_Suppliers_Invoice_payment.Data("Selection Rule(1)")="Smallest Number Busy"
Set Process_Pay_Invoice=Model.Modules.Create("BasicProcess","Process",5400,3900)
Process_Pay_Invoice.Data("Name")="Pay Invoice"
Process_Pay_Invoice.Data("Action")="Seize Delay Release"
Process_Pay_Invoice.Data("DelayType")="Expression"
Process_Pay_Invoice.Data("Units")="Seconds"
Process_Pay_Invoice.Data("Expression")="POIS(562)"
Process_Pay_Invoice.Data("Resource Type(1)")="Set"
Process_Pay_Invoice.Data("Set Name(1)")="Set_Pay_Invoice"
Process_Pay_Invoice.Data("Quantity(1)")="1"
Process_Pay_Invoice.Data("Selection Rule(1)")="Smallest Number Busy"
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

                    
Model.ReplicationLength = 8

Model.BaseTimeUnits = 2



