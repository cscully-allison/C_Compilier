from anytree import Node, RenderTree 
from anytree.exporter import DotExporter
PassUpNode47662512 = Node('TranslationUnit_2512')
PassUpNode47661776 = Node('TranslationUnit_1776', parent=PassUpNode47662512)
PassUpNode47625520 = Node('TranslationUnit_5520', parent=PassUpNode47661776)
PassUpNode47625872 = Node('ExternalDeclaration_5872', parent=PassUpNode47625520)
Declaration47625776 = Node('Declaration_5776', parent=PassUpNode47625872)
DeclarationSpecifiers47625616 = Node('DeclarationSpecifiers_5616', parent=Declaration47625776)
leaf = Node('int_5616', parent=DeclarationSpecifiers47625616)
InitDeclList47661808 = Node('InitDeclList_1808', parent=Declaration47625776)
PassUpNode47625680 = Node('Declarator_5680', parent=InitDeclList47661808)
FunctionPrototype47661168 = Node('FunctionPrototype_1168', parent=PassUpNode47625680)
PassUpNode47625712 = Node('DirectDeclarator_5712', parent=FunctionPrototype47661168)
Identifier47625808 = Node('Identifier_5808', parent=PassUpNode47625712)
leaf = Node('funct_5808', parent=Identifier47625808)
leaf = Node("TokenLocation=(2, 13, 5), Arguments=[{'Type Qualifier': ['const'], 'Type': ['int'], 'Array Size Info': ['10', '50', '20'], 'Subtype': 'Array Argument'}, {'Type': ['char']}, {'Type': ['int'], 'Array Size Info': ['30'], 'Subtype': 'Array Argument'}], Subtype='Function Prototype', Label='funct', Return Type=['int']", parent=Identifier47625808)
PassUpNode47628176 = Node('ParameterTypeList_8176', parent=FunctionPrototype47661168)
PassUpNode47627952 = Node('ParameterList_7952', parent=PassUpNode47628176)
PassUpNode47627408 = Node('ParameterList_7408', parent=PassUpNode47627952)
PassUpNode47626160 = Node('ParameterList_6160', parent=PassUpNode47627408)
PassUpNode47627984 = Node('ParameterDeclaration_7984', parent=PassUpNode47626160)
DeclarationSpecifiers47625840 = Node('DeclarationSpecifiers_5840', parent=PassUpNode47627984)
leaf = Node('const_5840', parent=DeclarationSpecifiers47625840)
DeclarationSpecifiers47626064 = Node('DeclarationSpecifiers_6064', parent=DeclarationSpecifiers47625840)
leaf = Node('int_6064', parent=DeclarationSpecifiers47626064)
PassUpNode47627376 = Node('AbstractDeclarator_7376', parent=PassUpNode47627984)
PassUpNode47627920 = Node('DirectAbstractDeclarator_7920', parent=PassUpNode47627376)
PassUpNode47627312 = Node('DirectAbstractDeclarator_7312', parent=PassUpNode47627920)
PassUpNode47626736 = Node('DirectAbstractDeclarator_6736', parent=PassUpNode47627312)
PassUpNode47626704 = Node('ConstantExpression_6704', parent=PassUpNode47626736)
PassUpNode47626672 = Node('ConditionalExpression_6672', parent=PassUpNode47626704)
PassUpNode47626640 = Node('LogicalOrExpression_6640', parent=PassUpNode47626672)
PassUpNode47626608 = Node('LogicalAndExpression_6608', parent=PassUpNode47626640)
PassUpNode47626576 = Node('InclusiveOrExpression_6576', parent=PassUpNode47626608)
PassUpNode47626544 = Node('ExclusiveOrExpression_6544', parent=PassUpNode47626576)
PassUpNode47626512 = Node('AndExpression_6512', parent=PassUpNode47626544)
PassUpNode47626480 = Node('EqalityExpression_6480', parent=PassUpNode47626512)
PassUpNode47626448 = Node('ShiftExpression_6448', parent=PassUpNode47626480)
PassUpNode47626416 = Node('ShiftExpression_6416', parent=PassUpNode47626448)
PassUpNode47626384 = Node('AdditiveExpression_6384', parent=PassUpNode47626416)
PassUpNode47626352 = Node('MultiplicativeExpression_6352', parent=PassUpNode47626384)
PassUpNode47626320 = Node('CastExpression_6320', parent=PassUpNode47626352)
PassUpNode47626000 = Node('UnaryExpression_6000', parent=PassUpNode47626320)
PassUpNode47626192 = Node('PostfixExpression_6192', parent=PassUpNode47626000)
PrimaryExpression47626224 = Node('PrimaryExpression_6224', parent=PassUpNode47626192)
Constant47625968 = Node('Constant_5968', parent=PrimaryExpression47626224)
leaf = Node('10_5968', parent=Constant47625968)
PassUpNode47627280 = Node('ConstantExpression_7280', parent=PassUpNode47627312)
PassUpNode47627248 = Node('ConditionalExpression_7248', parent=PassUpNode47627280)
PassUpNode47627216 = Node('LogicalOrExpression_7216', parent=PassUpNode47627248)
PassUpNode47627184 = Node('LogicalAndExpression_7184', parent=PassUpNode47627216)
PassUpNode47627152 = Node('InclusiveOrExpression_7152', parent=PassUpNode47627184)
PassUpNode47627120 = Node('ExclusiveOrExpression_7120', parent=PassUpNode47627152)
PassUpNode47627088 = Node('AndExpression_7088', parent=PassUpNode47627120)
PassUpNode47627056 = Node('EqalityExpression_7056', parent=PassUpNode47627088)
PassUpNode47627024 = Node('ShiftExpression_7024', parent=PassUpNode47627056)
PassUpNode47626992 = Node('ShiftExpression_6992', parent=PassUpNode47627024)
PassUpNode47626960 = Node('AdditiveExpression_6960', parent=PassUpNode47626992)
PassUpNode47626928 = Node('MultiplicativeExpression_6928', parent=PassUpNode47626960)
PassUpNode47626288 = Node('CastExpression_6288', parent=PassUpNode47626928)
PassUpNode47626768 = Node('UnaryExpression_6768', parent=PassUpNode47626288)
PassUpNode47626800 = Node('PostfixExpression_6800', parent=PassUpNode47626768)
PrimaryExpression47626832 = Node('PrimaryExpression_6832', parent=PassUpNode47626800)
Constant47626128 = Node('Constant_6128', parent=PrimaryExpression47626832)
leaf = Node('50_6128', parent=Constant47626128)
PassUpNode47627888 = Node('ConstantExpression_7888', parent=PassUpNode47627920)
PassUpNode47627856 = Node('ConditionalExpression_7856', parent=PassUpNode47627888)
PassUpNode47627824 = Node('LogicalOrExpression_7824', parent=PassUpNode47627856)
PassUpNode47627792 = Node('LogicalAndExpression_7792', parent=PassUpNode47627824)
PassUpNode47627760 = Node('InclusiveOrExpression_7760', parent=PassUpNode47627792)
PassUpNode47627728 = Node('ExclusiveOrExpression_7728', parent=PassUpNode47627760)
PassUpNode47627696 = Node('AndExpression_7696', parent=PassUpNode47627728)
PassUpNode47627664 = Node('EqalityExpression_7664', parent=PassUpNode47627696)
PassUpNode47627632 = Node('ShiftExpression_7632', parent=PassUpNode47627664)
PassUpNode47627600 = Node('ShiftExpression_7600', parent=PassUpNode47627632)
PassUpNode47627568 = Node('AdditiveExpression_7568', parent=PassUpNode47627600)
PassUpNode47626896 = Node('MultiplicativeExpression_6896', parent=PassUpNode47627568)
PassUpNode47627344 = Node('CastExpression_7344', parent=PassUpNode47626896)
PassUpNode47625904 = Node('UnaryExpression_5904', parent=PassUpNode47627344)
PassUpNode47627440 = Node('PostfixExpression_7440', parent=PassUpNode47625904)
PrimaryExpression47627472 = Node('PrimaryExpression_7472', parent=PassUpNode47627440)
Constant47625936 = Node('Constant_5936', parent=PrimaryExpression47627472)
leaf = Node('20_5936', parent=Constant47625936)
PassUpNode47628048 = Node('ParameterDeclaration_8048', parent=PassUpNode47627408)
DeclarationSpecifiers47627536 = Node('DeclarationSpecifiers_7536', parent=PassUpNode47628048)
leaf = Node('char_7536', parent=DeclarationSpecifiers47627536)
PassUpNode47661712 = Node('ParameterDeclaration_1712', parent=PassUpNode47627952)
DeclarationSpecifiers47628240 = Node('DeclarationSpecifiers_8240', parent=PassUpNode47661712)
leaf = Node('int_8240', parent=DeclarationSpecifiers47628240)
PassUpNode47661104 = Node('AbstractDeclarator_1104', parent=PassUpNode47661712)
PassUpNode47661648 = Node('DirectAbstractDeclarator_1648', parent=PassUpNode47661104)
PassUpNode47661616 = Node('ConstantExpression_1616', parent=PassUpNode47661648)
PassUpNode47661584 = Node('ConditionalExpression_1584', parent=PassUpNode47661616)
PassUpNode47661552 = Node('LogicalOrExpression_1552', parent=PassUpNode47661584)
PassUpNode47661520 = Node('LogicalAndExpression_1520', parent=PassUpNode47661552)
PassUpNode47661488 = Node('InclusiveOrExpression_1488', parent=PassUpNode47661520)
PassUpNode47661456 = Node('ExclusiveOrExpression_1456', parent=PassUpNode47661488)
PassUpNode47661424 = Node('AndExpression_1424', parent=PassUpNode47661456)
PassUpNode47661392 = Node('EqalityExpression_1392', parent=PassUpNode47661424)
PassUpNode47661360 = Node('ShiftExpression_1360', parent=PassUpNode47661392)
PassUpNode47661328 = Node('ShiftExpression_1328', parent=PassUpNode47661360)
PassUpNode47661296 = Node('AdditiveExpression_1296', parent=PassUpNode47661328)
PassUpNode47661264 = Node('MultiplicativeExpression_1264', parent=PassUpNode47661296)
PassUpNode47661232 = Node('CastExpression_1232', parent=PassUpNode47661264)
PassUpNode47661200 = Node('UnaryExpression_1200', parent=PassUpNode47661232)
PassUpNode47628016 = Node('PostfixExpression_8016', parent=PassUpNode47661200)
PrimaryExpression47628144 = Node('PrimaryExpression_8144', parent=PassUpNode47628016)
Constant47628208 = Node('Constant_8208', parent=PrimaryExpression47628144)
leaf = Node('30_8208', parent=Constant47628208)
PassUpNode47662192 = Node('ExternalDeclaration_2192', parent=PassUpNode47661776)
FunctionDefintion47662544 = Node('FunctionDefintion_2544', parent=PassUpNode47662192)
DeclarationSpecifiers47661968 = Node('DeclarationSpecifiers_1968', parent=FunctionDefintion47662544)
leaf = Node('const_1968', parent=DeclarationSpecifiers47661968)
DeclarationSpecifiers47661680 = Node('DeclarationSpecifiers_1680', parent=DeclarationSpecifiers47661968)
leaf = Node('int_1680', parent=DeclarationSpecifiers47661680)
PassUpNode47661840 = Node('Declarator_1840', parent=FunctionDefintion47662544)
FunctionPrototype47662576 = Node('FunctionPrototype_2576', parent=PassUpNode47661840)
PassUpNode47662032 = Node('DirectDeclarator_2032', parent=FunctionPrototype47662576)
Identifier47661872 = Node('Identifier_1872', parent=PassUpNode47662032)
leaf = Node('main_1872', parent=Identifier47661872)
leaf = Node("TokenLocation=(5, 78, 11), Arguments=[{'Type Qualifier': ['const'], 'Type': ['int']}], Subtype='Function Prototype', Label='main'", parent=Identifier47661872)
PassUpNode47662448 = Node('ParameterTypeList_2448', parent=FunctionPrototype47662576)
PassUpNode47662416 = Node('ParameterList_2416', parent=PassUpNode47662448)
Declaration47662160 = Node('Declaration_2160', parent=PassUpNode47662416)
DeclarationSpecifiers47661936 = Node('DeclarationSpecifiers_1936', parent=Declaration47662160)
leaf = Node('const_1936', parent=DeclarationSpecifiers47661936)
DeclarationSpecifiers47662224 = Node('DeclarationSpecifiers_2224', parent=DeclarationSpecifiers47661936)
leaf = Node('int_2224', parent=DeclarationSpecifiers47662224)
PassUpNode47662384 = Node('Declarator_2384', parent=Declaration47662160)
PassUpNode47662288 = Node('DirectDeclarator_2288', parent=PassUpNode47662384)
Identifier47662096 = Node('Identifier_2096', parent=PassUpNode47662288)
leaf = Node('g_2096', parent=Identifier47662096)
leaf = Node("TokenLocation=(5, 93, 26), Type=['int'], Type Qualifier=['const']", parent=Identifier47662096)
CompoundStatement47716496 = Node('CompoundStatement_6496', parent=FunctionDefintion47662544)
DeclList47663440 = Node('DeclList_3440', parent=CompoundStatement47716496)
DeclList47663152 = Node('DeclList_3152', parent=DeclList47663440)
DeclList47662896 = Node('DeclList_2896', parent=DeclList47663152)
Declaration47662928 = Node('Declaration_2928', parent=DeclList47662896)
DeclarationSpecifiers47662736 = Node('DeclarationSpecifiers_2736', parent=Declaration47662928)
leaf = Node('static_2736', parent=DeclarationSpecifiers47662736)
DeclarationSpecifiers47662480 = Node('DeclarationSpecifiers_2480', parent=DeclarationSpecifiers47662736)
leaf = Node('int_2480', parent=DeclarationSpecifiers47662480)
InitDeclList47662832 = Node('InitDeclList_2832', parent=Declaration47662928)
PassUpNode47662864 = Node('Declarator_2864', parent=InitDeclList47662832)
PassUpNode47662768 = Node('DirectDeclarator_2768', parent=PassUpNode47662864)
Identifier47662320 = Node('Identifier_2320', parent=PassUpNode47662768)
leaf = Node('l_2320', parent=Identifier47662320)
leaf = Node("TokenLocation=(6, 112, 16), Type=['int'], Storage Class Specifier='static'", parent=Identifier47662320)
Declaration47663216 = Node('Declaration_3216', parent=DeclList47663152)
DeclarationSpecifiers47663024 = Node('DeclarationSpecifiers_3024', parent=Declaration47663216)
leaf = Node('char_3024', parent=DeclarationSpecifiers47663024)
InitDeclList47663184 = Node('InitDeclList_3184', parent=Declaration47663216)
PassUpNode47663120 = Node('Declarator_3120', parent=InitDeclList47663184)
PassUpNode47662960 = Node('DirectDeclarator_2960', parent=PassUpNode47663120)
Identifier47663088 = Node('Identifier_3088', parent=PassUpNode47662960)
leaf = Node('b_3088', parent=Identifier47663088)
leaf = Node("TokenLocation=(7, 124, 10), Type=['char']", parent=Identifier47663088)
Declaration47662800 = Node('Declaration_2800', parent=DeclList47663440)
DeclarationSpecifiers47663312 = Node('DeclarationSpecifiers_3312', parent=Declaration47662800)
leaf = Node('int_3312', parent=DeclarationSpecifiers47663312)
InitDeclList47664176 = Node('InitDeclList_4176', parent=Declaration47662800)
PassUpNode47663056 = Node('Declarator_3056', parent=InitDeclList47664176)
ArrayDeclaration47664048 = Node('ArrayDeclaration_4048', parent=PassUpNode47663056)
PassUpNode47662608 = Node('DirectDeclarator_2608', parent=ArrayDeclaration47664048)
Identifier47663376 = Node('Identifier_3376', parent=PassUpNode47662608)
leaf = Node('arr_3376', parent=Identifier47663376)
leaf = Node("TokenLocation=(8, 135, 9), Array Size=['10'], Subtype='Array', Type=['int']", parent=Identifier47663376)
PassUpNode47664016 = Node('ConstantExpression_4016', parent=ArrayDeclaration47664048)
PassUpNode47663984 = Node('ConditionalExpression_3984', parent=PassUpNode47664016)
PassUpNode47663952 = Node('LogicalOrExpression_3952', parent=PassUpNode47663984)
PassUpNode47663920 = Node('LogicalAndExpression_3920', parent=PassUpNode47663952)
PassUpNode47663888 = Node('InclusiveOrExpression_3888', parent=PassUpNode47663920)
PassUpNode47663856 = Node('ExclusiveOrExpression_3856', parent=PassUpNode47663888)
PassUpNode47663824 = Node('AndExpression_3824', parent=PassUpNode47663856)
PassUpNode47663792 = Node('EqalityExpression_3792', parent=PassUpNode47663824)
PassUpNode47663760 = Node('ShiftExpression_3760', parent=PassUpNode47663792)
PassUpNode47663728 = Node('ShiftExpression_3728', parent=PassUpNode47663760)
PassUpNode47663696 = Node('AdditiveExpression_3696', parent=PassUpNode47663728)
PassUpNode47663664 = Node('MultiplicativeExpression_3664', parent=PassUpNode47663696)
PassUpNode47663632 = Node('CastExpression_3632', parent=PassUpNode47663664)
PassUpNode47663600 = Node('UnaryExpression_3600', parent=PassUpNode47663632)
PassUpNode47663472 = Node('PostfixExpression_3472', parent=PassUpNode47663600)
PrimaryExpression47663504 = Node('PrimaryExpression_3504', parent=PassUpNode47663472)
Constant47663408 = Node('Constant_3408', parent=PrimaryExpression47663504)
leaf = Node('10_3408', parent=Constant47663408)
PassUpNode47716528 = Node('StatementList_6528', parent=CompoundStatement47716496)
PassUpNode47715792 = Node('StatementList_5792', parent=PassUpNode47716528)
PassUpNode47715760 = Node('Statement_5760', parent=PassUpNode47715792)
PassUpNode47715696 = Node('Expression_5696', parent=PassUpNode47715760)
PassUpNode47715664 = Node('AssignmentExpression_5664', parent=PassUpNode47715696)
PassUpNode47715632 = Node('ConditionalExpression_5632', parent=PassUpNode47715664)
PassUpNode47715600 = Node('LogicalOrExpression_5600', parent=PassUpNode47715632)
PassUpNode47715568 = Node('LogicalAndExpression_5568', parent=PassUpNode47715600)
PassUpNode47715536 = Node('InclusiveOrExpression_5536', parent=PassUpNode47715568)
PassUpNode47715504 = Node('ExclusiveOrExpression_5504', parent=PassUpNode47715536)
PassUpNode47715472 = Node('AndExpression_5472', parent=PassUpNode47715504)
PassUpNode47715440 = Node('EqalityExpression_5440', parent=PassUpNode47715472)
PassUpNode47714864 = Node('ShiftExpression_4864', parent=PassUpNode47715440)
PassUpNode47715344 = Node('ShiftExpression_5344', parent=PassUpNode47714864)
PassUpNode47662672 = Node('AdditiveExpression_2672', parent=PassUpNode47715344)
PassUpNode47714768 = Node('MultiplicativeExpression_4768', parent=PassUpNode47662672)
PassUpNode47715376 = Node('CastExpression_5376', parent=PassUpNode47714768)
PassUpNode47664304 = Node('UnaryExpression_4304', parent=PassUpNode47715376)
FunctionCall47665040 = Node('FunctionCall_5040', parent=PassUpNode47664304)
PassUpNode47663344 = Node('PostfixExpression_3344', parent=FunctionCall47665040)
PrimaryExpression47664240 = Node('PrimaryExpression_4240', parent=PassUpNode47663344)
Identifier47664080 = Node('Identifier_4080', parent=PrimaryExpression47664240)
leaf = Node('funct_4080', parent=Identifier47664080)
PassUpNode47715280 = Node('ArgumentExpressionList_5280', parent=FunctionCall47665040)
PassUpNode47714704 = Node('ArgumentExpressionList_4704', parent=PassUpNode47715280)
PassUpNode47664880 = Node('ArgumentExpressionList_4880', parent=PassUpNode47714704)
PassUpNode47664848 = Node('AssignmentExpression_4848', parent=PassUpNode47664880)
PassUpNode47664816 = Node('ConditionalExpression_4816', parent=PassUpNode47664848)
PassUpNode47664784 = Node('LogicalOrExpression_4784', parent=PassUpNode47664816)
PassUpNode47664752 = Node('LogicalAndExpression_4752', parent=PassUpNode47664784)
PassUpNode47664720 = Node('InclusiveOrExpression_4720', parent=PassUpNode47664752)
PassUpNode47664688 = Node('ExclusiveOrExpression_4688', parent=PassUpNode47664720)
PassUpNode47664656 = Node('AndExpression_4656', parent=PassUpNode47664688)
PassUpNode47664624 = Node('EqalityExpression_4624', parent=PassUpNode47664656)
PassUpNode47664592 = Node('ShiftExpression_4592', parent=PassUpNode47664624)
PassUpNode47664560 = Node('ShiftExpression_4560', parent=PassUpNode47664592)
PassUpNode47664528 = Node('AdditiveExpression_4528', parent=PassUpNode47664560)
PassUpNode47664432 = Node('MultiplicativeExpression_4432', parent=PassUpNode47664528)
PassUpNode47664400 = Node('CastExpression_4400', parent=PassUpNode47664432)
PassUpNode47664464 = Node('UnaryExpression_4464', parent=PassUpNode47664400)
PassUpNode47664208 = Node('PostfixExpression_4208', parent=PassUpNode47664464)
PrimaryExpression47664272 = Node('PrimaryExpression_4272', parent=PassUpNode47664208)
Identifier47664144 = Node('Identifier_4144', parent=PrimaryExpression47664272)
leaf = Node('arr_4144', parent=Identifier47664144)
leaf = Node("TokenLocation=(8, 135, 9), Array Size=['10'], Subtype='Array', Type=['int']", parent=Identifier47664144)
PassUpNode47714672 = Node('AssignmentExpression_4672', parent=PassUpNode47714704)
PassUpNode47714640 = Node('ConditionalExpression_4640', parent=PassUpNode47714672)
PassUpNode47714608 = Node('LogicalOrExpression_4608', parent=PassUpNode47714640)
PassUpNode47714576 = Node('LogicalAndExpression_4576', parent=PassUpNode47714608)
PassUpNode47714544 = Node('InclusiveOrExpression_4544', parent=PassUpNode47714576)
PassUpNode47714512 = Node('ExclusiveOrExpression_4512', parent=PassUpNode47714544)
PassUpNode47714480 = Node('AndExpression_4480', parent=PassUpNode47714512)
PassUpNode47714448 = Node('EqalityExpression_4448', parent=PassUpNode47714480)
PassUpNode47714416 = Node('ShiftExpression_4416', parent=PassUpNode47714448)
PassUpNode47714384 = Node('ShiftExpression_4384', parent=PassUpNode47714416)
PassUpNode47714352 = Node('AdditiveExpression_4352', parent=PassUpNode47714384)
PassUpNode47665136 = Node('MultiplicativeExpression_5136', parent=PassUpNode47714352)
PassUpNode47665104 = Node('CastExpression_5104', parent=PassUpNode47665136)
PassUpNode47665072 = Node('UnaryExpression_5072', parent=PassUpNode47665104)
PassUpNode47664976 = Node('PostfixExpression_4976', parent=PassUpNode47665072)
PrimaryExpression47665008 = Node('PrimaryExpression_5008', parent=PassUpNode47664976)
Constant47664912 = Node('Constant_4912', parent=PrimaryExpression47665008)
leaf = Node('4_4912', parent=Constant47664912)
PassUpNode47715248 = Node('AssignmentExpression_5248', parent=PassUpNode47715280)
PassUpNode47715216 = Node('ConditionalExpression_5216', parent=PassUpNode47715248)
PassUpNode47715184 = Node('LogicalOrExpression_5184', parent=PassUpNode47715216)
PassUpNode47715152 = Node('LogicalAndExpression_5152', parent=PassUpNode47715184)
PassUpNode47715120 = Node('InclusiveOrExpression_5120', parent=PassUpNode47715152)
PassUpNode47715088 = Node('ExclusiveOrExpression_5088', parent=PassUpNode47715120)
PassUpNode47715056 = Node('AndExpression_5056', parent=PassUpNode47715088)
PassUpNode47715024 = Node('EqalityExpression_5024', parent=PassUpNode47715056)
PassUpNode47714992 = Node('ShiftExpression_4992', parent=PassUpNode47715024)
PassUpNode47714960 = Node('ShiftExpression_4960', parent=PassUpNode47714992)
PassUpNode47714928 = Node('AdditiveExpression_4928', parent=PassUpNode47714960)
PassUpNode47714896 = Node('MultiplicativeExpression_4896', parent=PassUpNode47714928)
PassUpNode47714736 = Node('CastExpression_4736', parent=PassUpNode47714896)
PassUpNode47664496 = Node('UnaryExpression_4496', parent=PassUpNode47714736)
PassUpNode47714800 = Node('PostfixExpression_4800', parent=PassUpNode47664496)
PrimaryExpression47714832 = Node('PrimaryExpression_4832', parent=PassUpNode47714800)
Constant47664944 = Node('Constant_4944', parent=PrimaryExpression47714832)
leaf = Node('1_4944', parent=Constant47664944)
PassUpNode47664112 = Node('Statement_4112', parent=PassUpNode47716528)
PassUpNode47716464 = Node('ExternalDeclaration_6464', parent=PassUpNode47662512)
FunctionDefintion47751248 = Node('FunctionDefintion_1248', parent=PassUpNode47716464)
DeclarationSpecifiers47715888 = Node('DeclarationSpecifiers_5888', parent=FunctionDefintion47751248)
leaf = Node('int_5888', parent=DeclarationSpecifiers47715888)
PassUpNode47715952 = Node('Declarator_5952', parent=FunctionDefintion47751248)
FunctionPrototype47751536 = Node('FunctionPrototype_1536', parent=PassUpNode47715952)
PassUpNode47662000 = Node('DirectDeclarator_2000', parent=FunctionPrototype47751536)
Identifier47628112 = Node('Identifier_8112', parent=PassUpNode47662000)
leaf = Node('funct_8112', parent=Identifier47628112)
leaf = Node("TokenLocation=(2, 13, 5), Arguments=[{'Type Qualifier': ['const'], 'Type': ['int'], 'Array Size Info': ['10', '50', '20'], 'Subtype': 'Array Argument'}, {'Type': ['char']}, {'Type': ['int'], 'Array Size Info': ['30'], 'Subtype': 'Array Argument'}], Subtype='Function Prototype', Label='funct', Return Type=['int']", parent=Identifier47628112)
PassUpNode47718320 = Node('ParameterTypeList_8320', parent=FunctionPrototype47751536)
PassUpNode47718128 = Node('ParameterList_8128', parent=PassUpNode47718320)
PassUpNode47717584 = Node('ParameterList_7584', parent=PassUpNode47718128)
PassUpNode47716144 = Node('ParameterList_6144', parent=PassUpNode47717584)
Declaration47718160 = Node('Declaration_8160', parent=PassUpNode47716144)
DeclarationSpecifiers47716432 = Node('DeclarationSpecifiers_6432', parent=Declaration47718160)
leaf = Node('const_6432', parent=DeclarationSpecifiers47716432)
DeclarationSpecifiers47716336 = Node('DeclarationSpecifiers_6336', parent=DeclarationSpecifiers47716432)
leaf = Node('int_6336', parent=DeclarationSpecifiers47716336)
PassUpNode47717552 = Node('Declarator_7552', parent=Declaration47718160)
ArrayDeclaration47718096 = Node('ArrayDeclaration_8096', parent=PassUpNode47717552)
ArrayDeclaration47717488 = Node('ArrayDeclaration_7488', parent=ArrayDeclaration47718096)
ArrayDeclaration47716880 = Node('ArrayDeclaration_6880', parent=ArrayDeclaration47717488)
PassUpNode47716272 = Node('DirectDeclarator_6272', parent=ArrayDeclaration47716880)
Identifier47716592 = Node('Identifier_6592', parent=PassUpNode47716272)
leaf = Node('a_6592', parent=Identifier47716592)
leaf = Node("TokenLocation=(18, 232, 21), Array Size=['10', '50', '20'], Subtype='Array', Type=['int'], Type Qualifier=['const']", parent=Identifier47716592)
PassUpNode47716848 = Node('ConstantExpression_6848', parent=ArrayDeclaration47716880)
PassUpNode47716816 = Node('ConditionalExpression_6816', parent=PassUpNode47716848)
PassUpNode47716784 = Node('LogicalOrExpression_6784', parent=PassUpNode47716816)
PassUpNode47716752 = Node('LogicalAndExpression_6752', parent=PassUpNode47716784)
PassUpNode47716720 = Node('InclusiveOrExpression_6720', parent=PassUpNode47716752)
PassUpNode47716688 = Node('ExclusiveOrExpression_6688', parent=PassUpNode47716720)
PassUpNode47716656 = Node('AndExpression_6656', parent=PassUpNode47716688)
PassUpNode47716624 = Node('EqalityExpression_6624', parent=PassUpNode47716656)
PassUpNode47716560 = Node('ShiftExpression_6560', parent=PassUpNode47716624)
PassUpNode47715920 = Node('ShiftExpression_5920', parent=PassUpNode47716560)
PassUpNode47715984 = Node('AdditiveExpression_5984', parent=PassUpNode47715920)
PassUpNode47716016 = Node('MultiplicativeExpression_6016', parent=PassUpNode47715984)
PassUpNode47716048 = Node('CastExpression_6048', parent=PassUpNode47716016)
PassUpNode47716080 = Node('UnaryExpression_6080', parent=PassUpNode47716048)
PassUpNode47716400 = Node('PostfixExpression_6400', parent=PassUpNode47716080)
PrimaryExpression47715824 = Node('PrimaryExpression_5824', parent=PassUpNode47716400)
Constant47716176 = Node('Constant_6176', parent=PrimaryExpression47715824)
leaf = Node('10_6176', parent=Constant47716176)
PassUpNode47717456 = Node('ConstantExpression_7456', parent=ArrayDeclaration47717488)
PassUpNode47717424 = Node('ConditionalExpression_7424', parent=PassUpNode47717456)
PassUpNode47717392 = Node('LogicalOrExpression_7392', parent=PassUpNode47717424)
PassUpNode47717360 = Node('LogicalAndExpression_7360', parent=PassUpNode47717392)
PassUpNode47717328 = Node('InclusiveOrExpression_7328', parent=PassUpNode47717360)
PassUpNode47717296 = Node('ExclusiveOrExpression_7296', parent=PassUpNode47717328)
PassUpNode47717264 = Node('AndExpression_7264', parent=PassUpNode47717296)
PassUpNode47717232 = Node('EqalityExpression_7232', parent=PassUpNode47717264)
PassUpNode47717200 = Node('ShiftExpression_7200', parent=PassUpNode47717232)
PassUpNode47717168 = Node('ShiftExpression_7168', parent=PassUpNode47717200)
PassUpNode47717136 = Node('AdditiveExpression_7136', parent=PassUpNode47717168)
PassUpNode47716112 = Node('MultiplicativeExpression_6112', parent=PassUpNode47717136)
PassUpNode47716912 = Node('CastExpression_6912', parent=PassUpNode47716112)
PassUpNode47716240 = Node('UnaryExpression_6240', parent=PassUpNode47716912)
PassUpNode47717008 = Node('PostfixExpression_7008', parent=PassUpNode47716240)
PrimaryExpression47717040 = Node('PrimaryExpression_7040', parent=PassUpNode47717008)
Constant47715408 = Node('Constant_5408', parent=PrimaryExpression47717040)
leaf = Node('50_5408', parent=Constant47715408)
PassUpNode47718064 = Node('ConstantExpression_8064', parent=ArrayDeclaration47718096)
PassUpNode47718032 = Node('ConditionalExpression_8032', parent=PassUpNode47718064)
PassUpNode47718000 = Node('LogicalOrExpression_8000', parent=PassUpNode47718032)
PassUpNode47717968 = Node('LogicalAndExpression_7968', parent=PassUpNode47718000)
PassUpNode47717936 = Node('InclusiveOrExpression_7936', parent=PassUpNode47717968)
PassUpNode47717904 = Node('ExclusiveOrExpression_7904', parent=PassUpNode47717936)
PassUpNode47717872 = Node('AndExpression_7872', parent=PassUpNode47717904)
PassUpNode47717840 = Node('EqalityExpression_7840', parent=PassUpNode47717872)
PassUpNode47717808 = Node('ShiftExpression_7808', parent=PassUpNode47717840)
PassUpNode47717776 = Node('ShiftExpression_7776', parent=PassUpNode47717808)
PassUpNode47717744 = Node('AdditiveExpression_7744', parent=PassUpNode47717776)
PassUpNode47717104 = Node('MultiplicativeExpression_7104', parent=PassUpNode47717744)
PassUpNode47717520 = Node('CastExpression_7520', parent=PassUpNode47717104)
PassUpNode47716976 = Node('UnaryExpression_6976', parent=PassUpNode47717520)
PassUpNode47717616 = Node('PostfixExpression_7616', parent=PassUpNode47716976)
PrimaryExpression47717648 = Node('PrimaryExpression_7648', parent=PassUpNode47717616)
Constant47716944 = Node('Constant_6944', parent=PrimaryExpression47717648)
leaf = Node('20_6944', parent=Constant47716944)
Declaration47718224 = Node('Declaration_8224', parent=PassUpNode47717584)
DeclarationSpecifiers47717712 = Node('DeclarationSpecifiers_7712', parent=Declaration47718224)
leaf = Node('char_7712', parent=DeclarationSpecifiers47717712)
PassUpNode47718384 = Node('Declarator_8384', parent=Declaration47718224)
PassUpNode47718288 = Node('DirectDeclarator_8288', parent=PassUpNode47718384)
Identifier47718352 = Node('Identifier_8352', parent=PassUpNode47718288)
leaf = Node('d_8352', parent=Identifier47718352)
leaf = Node("TokenLocation=(18, 252, 41), Type=['char']", parent=Identifier47718352)
Declaration47752080 = Node('Declaration_2080', parent=PassUpNode47718128)
DeclarationSpecifiers47718192 = Node('DeclarationSpecifiers_8192', parent=Declaration47752080)
leaf = Node('int_8192', parent=DeclarationSpecifiers47718192)
PassUpNode47751216 = Node('Declarator_1216', parent=Declaration47752080)
ArrayDeclaration47752016 = Node('ArrayDeclaration_2016', parent=PassUpNode47751216)
PassUpNode47751376 = Node('DirectDeclarator_1376', parent=ArrayDeclaration47752016)
Identifier47751504 = Node('Identifier_1504', parent=PassUpNode47751376)
leaf = Node('f_1504', parent=Identifier47751504)
leaf = Node("TokenLocation=(18, 259, 48), Array Size=['30'], Subtype='Array', Type=['int']", parent=Identifier47751504)
PassUpNode47751984 = Node('ConstantExpression_1984', parent=ArrayDeclaration47752016)
PassUpNode47751952 = Node('ConditionalExpression_1952', parent=PassUpNode47751984)
PassUpNode47751920 = Node('LogicalOrExpression_1920', parent=PassUpNode47751952)
PassUpNode47751888 = Node('LogicalAndExpression_1888', parent=PassUpNode47751920)
PassUpNode47751856 = Node('InclusiveOrExpression_1856', parent=PassUpNode47751888)
PassUpNode47751824 = Node('ExclusiveOrExpression_1824', parent=PassUpNode47751856)
PassUpNode47751792 = Node('AndExpression_1792', parent=PassUpNode47751824)
PassUpNode47751760 = Node('EqalityExpression_1760', parent=PassUpNode47751792)
PassUpNode47751728 = Node('ShiftExpression_1728', parent=PassUpNode47751760)
PassUpNode47751696 = Node('ShiftExpression_1696', parent=PassUpNode47751728)
PassUpNode47751664 = Node('AdditiveExpression_1664', parent=PassUpNode47751696)
PassUpNode47751632 = Node('MultiplicativeExpression_1632', parent=PassUpNode47751664)
PassUpNode47751600 = Node('CastExpression_1600', parent=PassUpNode47751632)
PassUpNode47751568 = Node('UnaryExpression_1568', parent=PassUpNode47751600)
PassUpNode47751472 = Node('PostfixExpression_1472', parent=PassUpNode47751568)
PrimaryExpression47751408 = Node('PrimaryExpression_1408', parent=PassUpNode47751472)
Constant47751312 = Node('Constant_1312', parent=PrimaryExpression47751408)
leaf = Node('30_1312', parent=Constant47751312)
CompoundStatement47751280 = Node('CompoundStatement_1280', parent=FunctionDefintion47751248)

for pre, fill, node in RenderTree(PassUpNode47662512):
    if "TokenLocation" in node.name: print("%s%s" % (pre, node.name))
    else: print("%s%s" % (pre, node.name[:-5]) )

    
def f(node):
    if node.is_leaf and "TokenLocation" in node.name:
        return 'label="%s"' % (node.name)
    return 'label="%s"' % (node.name[:-5])

DotExporter(PassUpNode47662512, nodeattrfunc=f).to_picture("AST.png")
        