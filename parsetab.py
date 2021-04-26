
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BIGGEREQUALSTHAN BIGGERTHAN BOOL CLASS CLOSEBRACKET CLOSECURLY CLOSEPAREN COMMA CONSTRUCTOR CTEFLOAT CTEINT CTESTRING DIFFERENTTHAN DIV DOT ELSE EQUALS FALSE FLOAT FUNC ID IF INPUT INT MAIN OPENBRACKET OPENCURLY OPENPAREN OR OUTPUT PROGRAM RETURN SAMEAS SEMICOLON SMALLEQUALSTHAN SMALLTHAN STRING SUBTRACT SUM TIMES TRUE TWODOTS VAR WHILE\n        program     : PROGRAM ID save_program SEMICOLON altprogram\n        altprogram  : class altprogram\n                    | var altprogram\n                    | function altprogram\n                    | main\n         save_program : \n        main    : MAIN save_main OPENPAREN CLOSEPAREN OPENCURLY altmain\n        altmain : var altmain\n                | estatuto altmain\n                | CLOSECURLY clear_scope\n         save_main :  clear_scope : \n        class     : CLASS ID altclass save_class OPENCURLY alt2class\n        altclass  : TWODOTS ID\n                  | empty\n        alt2class : var alt2class\n                  | function alt2class\n                  | constructor CLOSECURLY SEMICOLON remove_class_scope\n         save_class :  remove_class_scope : \n        constructor : CONSTRUCTOR save_constructor OPENPAREN altconst CLOSEPAREN OPENCURLY alt2const\n        altconst    : params altconst\n                    | empty\n        alt2const   : var alt2const\n                    | estatuto alt2const\n                    | CLOSECURLY remove_constructor_scope\n         save_constructor :  remove_constructor_scope : \n        var : VAR listids TWODOTS type save_vars SEMICOLON\n        \n        save_vars :\n        \n        listids      : ID save_var_name listidsalty\n        listidsalty : COMMA listids\n                    | OPENBRACKET CTEINT CLOSEBRACKET listidsaltz\n                    | empty\n        listidsaltz : COMMA listids\n                    | OPENBRACKET CTEINT CLOSEBRACKET listidsaltp\n                    | empty\n        listidsaltp : COMMA listids\n                    | empty\n        \n        save_var_name :\n        \n        function : FUNC ID OPENPAREN altfunc  CLOSEPAREN alt2func save_function OPENCURLY alt3func\n        altfunc  : params\n                 | empty\n        alt2func : TWODOTS type\n                 | empty\n        alt3func : var alt3func\n                 | estatuto alt3func\n                 | CLOSECURLY remove_function_scope\n         save_function :  remove_function_scope : \n        params      : ID TWODOTS type save_params altparams\n        altparams   : COMMA ID TWODOTS type save_params altparams\n                    | empty\n        \n        save_params :\n        \n        callfunc    : ID OPENPAREN altcall CLOSEPAREN\n        altcall     : expresion alt2call\n                    | empty\n        alt2call   : COMMA altcall\n                    | empty\n        \n        type : INT\n             | FLOAT\n             | STRING\n             | ID\n             | BOOL\n        \n        estatuto : assign\n                | condition\n                | write\n                | read\n                | return\n                | voidcall\n                | while\n        \n        voidcall : ID OPENPAREN CLOSEPAREN\n                | ID OPENPAREN expresion altcall\n        altcall : COMMA expresion altcall\n                | CLOSEPAREN SEMICOLON\n        \n        while    : WHILE OPENPAREN expresion CLOSEPAREN OPENCURLY altwhile\n        altwhile : estatuto altwhile\n                | CLOSECURLY\n        \n        varcall : varcte\n                | varcomplicated\n        \n        varcte : TRUE\n                | FALSE\n              | CTEFLOAT\n             | CTESTRING\n             | CTEINT\n        \n        varcomplicated : varcomp1\n                        | callfunc\n        varcomp1        : ID varcomp2\n        varcomp2        : DOT varcomp3\n                        | empty\n        varcomp3        : varcomp1\n                        | callfunc\n        \n        expresion       : exp altexpresion\n        altexpresion    : altexpresion2 exp\n                        | empty\n        altexpresion2   : SAMEAS\n                        | BIGGERTHAN\n                        | BIGGEREQUALSTHAN\n                        | SMALLTHAN\n                        | SMALLEQUALSTHAN\n                        | DIFFERENTTHAN\n                        | AND\n                        | OR\n        \n        exp     : termino\n                | termino altexp\n        altexp  : SUM termino altexp\n                | SUBTRACT termino altexp\n                | empty\n        \n        termino     : factor\n                    | factor alttermino\n        alttermino : TIMES factor alttermino\n                    | DIV factor alttermino\n                    | empty\n        \n        read : INPUT OPENPAREN ID CLOSEPAREN SEMICOLON\n        \n        write : OUTPUT OPENPAREN varcall altwrite\n                | OUTPUT OPENPAREN expresion altwrite\n        altwrite : COMMA varcall altwrite\n                | COMMA expresion altwrite\n                | CLOSEPAREN SEMICOLON\n        \n        factor : OPENPAREN expresion CLOSEPAREN  \n                | SUM varcall\n                | SUBTRACT varcall\n                | varcall\n        \n        condition : IF OPENPAREN expresion CLOSEPAREN OPENCURLY altcondition\n                    | IF OPENPAREN expresion CLOSEPAREN  OPENCURLY  altcondition ELSE OPENCURLY altcondition\n        altcondition : estatuto altcondition\n                    | CLOSECURLY\n        \n        assign : ID assign1 EQUALS expresion SEMICOLON\n        assign1 : DOT ID assign1\n                | empty\n        \n        return  : RETURN expresion SEMICOLON\n        \n        empty :\n        '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,6,10,15,16,17,65,68,93,94,95,],[0,-1,-5,-2,-3,-4,-7,-12,-8,-9,-10,]),'ID':([2,11,12,13,24,26,28,33,34,35,36,37,39,51,53,59,61,63,66,67,69,70,71,72,73,74,75,80,88,90,97,98,100,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,123,126,127,128,129,130,131,132,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,163,164,168,173,174,177,178,179,180,184,185,187,189,190,191,192,193,194,196,197,198,203,205,209,210,211,212,213,214,215,218,219,220,221,222,223,224,225,226,228,229,230,231,232,233,234,235,236,237,238,240,241,243,245,246,250,251,252,],[3,18,20,21,31,36,42,-60,-61,-62,-63,-64,20,36,76,-29,-54,36,76,76,-65,-66,-67,-68,-69,-70,-71,120,20,-132,120,133,120,120,137,-132,-104,-109,120,120,-123,120,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,120,42,-51,171,-53,76,120,-72,120,-131,-93,120,-95,-96,-97,-98,-99,-100,-101,-102,-103,-105,120,120,-108,-110,120,120,-113,-121,-122,-88,120,120,-90,42,76,76,-132,-73,-57,120,-115,120,-116,-94,-132,-132,-132,-132,-120,-89,-91,-92,20,36,-128,-56,120,-59,120,-75,76,-119,-114,-106,-107,-111,-112,-55,76,76,-54,-58,-74,-124,76,-127,-117,-118,-76,76,-78,76,76,-132,-126,-77,-52,76,-125,]),'SEMICOLON':([3,4,32,33,34,35,36,37,48,84,103,104,105,106,109,111,112,113,114,115,116,117,118,119,120,139,141,150,153,154,157,159,160,161,164,176,181,186,188,189,190,191,192,193,194,196,197,198,220,221,222,223,224,],[-6,5,-30,-60,-61,-62,-63,-64,59,122,138,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-93,-95,-105,-108,-110,-113,-121,-122,-88,-90,209,214,218,219,-94,-132,-132,-132,-132,-120,-89,-91,-92,-106,-107,-111,-112,-55,]),'CLASS':([5,7,8,9,54,59,82,83,122,166,172,175,206,207,208,],[11,11,11,11,-13,-29,-16,-17,-20,-18,-41,-50,-46,-47,-48,]),'VAR':([5,7,8,9,47,53,54,55,56,59,66,67,69,70,71,72,73,74,75,82,83,104,105,106,109,111,112,113,114,115,116,117,118,119,120,122,129,131,132,138,139,141,150,153,154,157,159,160,161,164,166,172,173,174,175,177,178,179,184,187,189,190,191,192,193,194,196,197,198,206,207,208,209,210,211,212,213,214,218,219,220,221,222,223,224,226,229,230,231,233,234,235,236,238,240,241,245,246,252,],[12,12,12,12,12,12,-13,12,12,-29,12,12,-65,-66,-67,-68,-69,-70,-71,-16,-17,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-20,12,-72,-132,-131,-93,-95,-105,-108,-110,-113,-121,-122,-88,-90,-18,-41,12,12,-50,-132,-73,-57,-115,-116,-94,-132,-132,-132,-132,-120,-89,-91,-92,-46,-47,-48,-128,-56,-132,-59,-132,-75,-119,-114,-106,-107,-111,-112,-55,12,-58,-74,-124,-127,-117,-118,-76,-78,12,12,-126,-77,-125,]),'FUNC':([5,7,8,9,47,54,55,56,59,82,83,122,166,172,175,206,207,208,],[13,13,13,13,13,-13,13,13,-29,-16,-17,-20,-18,-41,-50,-46,-47,-48,]),'MAIN':([5,7,8,9,54,59,82,83,122,166,172,175,206,207,208,],[14,14,14,14,-13,-29,-16,-17,-20,-18,-41,-50,-46,-47,-48,]),'OPENPAREN':([14,21,22,58,76,77,78,79,80,81,85,97,100,101,104,105,106,107,109,111,112,113,114,115,116,117,118,119,120,121,130,132,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164,180,185,189,190,191,192,193,194,196,197,198,211,213,220,221,222,223,224,],[-11,28,29,-27,97,100,101,102,107,121,123,107,107,107,-132,-104,-109,107,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,162,107,107,107,-93,107,-95,-96,-97,-98,-99,-100,-101,-102,-103,-105,107,107,-108,-110,107,107,-113,-121,-122,-88,107,-90,107,107,-94,-132,-132,-132,-132,-120,-89,-91,-92,107,107,-106,-107,-111,-112,-55,]),'TWODOTS':([18,19,20,27,38,41,42,49,52,60,87,89,125,170,171,202,204,227,],[24,26,-40,-132,-31,-34,51,-32,63,-132,-33,-37,-35,-132,205,-36,-39,-38,]),'OPENCURLY':([18,23,25,30,31,33,34,35,36,37,46,52,62,64,91,92,183,199,200,244,],[-132,-19,-15,47,-14,-60,-61,-62,-63,-64,53,-132,-49,-45,129,-44,215,225,226,251,]),'COMMA':([20,27,33,34,35,36,37,60,61,90,104,105,106,109,111,112,113,114,115,116,117,118,119,120,132,135,136,139,141,150,153,154,157,159,160,161,162,164,170,177,189,190,191,192,193,194,196,197,198,211,213,216,217,220,221,222,223,224,228,243,],[-40,39,-60,-61,-62,-63,-64,88,-54,127,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,180,185,185,-93,-95,-105,-108,-110,-113,-121,-122,-88,180,-90,203,211,-94,-132,-132,-132,-132,-120,-89,-91,-92,180,180,185,185,-106,-107,-111,-112,-55,-54,127,]),'OPENBRACKET':([20,27,60,],[-40,40,86,]),'INT':([26,51,63,205,],[33,33,33,33,]),'FLOAT':([26,51,63,205,],[34,34,34,34,]),'STRING':([26,51,63,205,],[35,35,35,35,]),'BOOL':([26,51,63,205,],[37,37,37,37,]),'CLOSEPAREN':([28,29,33,34,35,36,37,43,44,45,61,90,97,104,105,106,109,111,112,113,114,115,116,117,118,119,120,123,126,128,132,134,135,136,137,139,141,150,153,154,157,158,159,160,161,162,164,165,167,168,169,177,179,189,190,191,192,193,194,195,196,197,198,201,210,211,212,213,214,216,217,220,221,222,223,224,228,229,230,243,250,],[-132,46,-60,-61,-62,-63,-64,52,-42,-43,-54,-132,131,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-132,-51,-53,181,183,186,186,188,-93,-95,-105,-108,-110,-113,194,-121,-122,-88,181,-90,199,200,-132,-23,-132,-57,-94,-132,-132,-132,-132,-120,224,-89,-91,-92,-22,-56,181,-59,181,-75,186,186,-106,-107,-111,-112,-55,-54,-58,-74,-132,-52,]),'CTEINT':([40,80,86,97,100,101,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,130,132,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164,180,185,189,190,191,192,193,194,196,197,198,211,213,220,221,222,223,224,],[50,117,124,117,117,117,-132,-104,-109,117,117,-123,117,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,117,117,117,-93,117,-95,-96,-97,-98,-99,-100,-101,-102,-103,-105,117,117,-108,-110,117,117,-113,-121,-122,-88,117,-90,117,117,-94,-132,-132,-132,-132,-120,-89,-91,-92,117,117,-106,-107,-111,-112,-55,]),'CONSTRUCTOR':([47,55,56,59,172,175,206,207,208,],[58,58,58,-29,-41,-50,-46,-47,-48,]),'CLOSEBRACKET':([50,124,],[60,170,]),'CLOSECURLY':([53,57,59,66,67,69,70,71,72,73,74,75,104,105,106,109,111,112,113,114,115,116,117,118,119,120,129,131,132,138,139,141,150,153,154,157,159,160,161,164,173,174,177,178,179,184,187,189,190,191,192,193,194,196,197,198,209,210,211,212,213,214,215,218,219,220,221,222,223,224,225,226,229,230,231,232,233,234,235,236,237,238,239,240,241,242,245,246,247,248,249,251,252,],[68,84,-29,68,68,-65,-66,-67,-68,-69,-70,-71,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,175,-72,-132,-131,-93,-95,-105,-108,-110,-113,-121,-122,-88,-90,175,175,-132,-73,-57,-115,-116,-94,-132,-132,-132,-132,-120,-89,-91,-92,-128,-56,-132,-59,-132,-75,233,-119,-114,-106,-107,-111,-112,-55,238,242,-58,-74,-124,233,-127,-117,-118,-76,238,-78,-21,242,242,-28,-126,-77,-24,-25,-26,233,-125,]),'IF':([53,59,66,67,69,70,71,72,73,74,75,104,105,106,109,111,112,113,114,115,116,117,118,119,120,129,131,132,138,139,141,150,153,154,157,159,160,161,164,173,174,177,178,179,184,187,189,190,191,192,193,194,196,197,198,209,210,211,212,213,214,215,218,219,220,221,222,223,224,225,226,229,230,231,232,233,234,235,236,237,238,240,241,245,246,251,252,],[77,-29,77,77,-65,-66,-67,-68,-69,-70,-71,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,77,-72,-132,-131,-93,-95,-105,-108,-110,-113,-121,-122,-88,-90,77,77,-132,-73,-57,-115,-116,-94,-132,-132,-132,-132,-120,-89,-91,-92,-128,-56,-132,-59,-132,-75,77,-119,-114,-106,-107,-111,-112,-55,77,77,-58,-74,-124,77,-127,-117,-118,-76,77,-78,77,77,-126,-77,77,-125,]),'OUTPUT':([53,59,66,67,69,70,71,72,73,74,75,104,105,106,109,111,112,113,114,115,116,117,118,119,120,129,131,132,138,139,141,150,153,154,157,159,160,161,164,173,174,177,178,179,184,187,189,190,191,192,193,194,196,197,198,209,210,211,212,213,214,215,218,219,220,221,222,223,224,225,226,229,230,231,232,233,234,235,236,237,238,240,241,245,246,251,252,],[78,-29,78,78,-65,-66,-67,-68,-69,-70,-71,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,78,-72,-132,-131,-93,-95,-105,-108,-110,-113,-121,-122,-88,-90,78,78,-132,-73,-57,-115,-116,-94,-132,-132,-132,-132,-120,-89,-91,-92,-128,-56,-132,-59,-132,-75,78,-119,-114,-106,-107,-111,-112,-55,78,78,-58,-74,-124,78,-127,-117,-118,-76,78,-78,78,78,-126,-77,78,-125,]),'INPUT':([53,59,66,67,69,70,71,72,73,74,75,104,105,106,109,111,112,113,114,115,116,117,118,119,120,129,131,132,138,139,141,150,153,154,157,159,160,161,164,173,174,177,178,179,184,187,189,190,191,192,193,194,196,197,198,209,210,211,212,213,214,215,218,219,220,221,222,223,224,225,226,229,230,231,232,233,234,235,236,237,238,240,241,245,246,251,252,],[79,-29,79,79,-65,-66,-67,-68,-69,-70,-71,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,79,-72,-132,-131,-93,-95,-105,-108,-110,-113,-121,-122,-88,-90,79,79,-132,-73,-57,-115,-116,-94,-132,-132,-132,-132,-120,-89,-91,-92,-128,-56,-132,-59,-132,-75,79,-119,-114,-106,-107,-111,-112,-55,79,79,-58,-74,-124,79,-127,-117,-118,-76,79,-78,79,79,-126,-77,79,-125,]),'RETURN':([53,59,66,67,69,70,71,72,73,74,75,104,105,106,109,111,112,113,114,115,116,117,118,119,120,129,131,132,138,139,141,150,153,154,157,159,160,161,164,173,174,177,178,179,184,187,189,190,191,192,193,194,196,197,198,209,210,211,212,213,214,215,218,219,220,221,222,223,224,225,226,229,230,231,232,233,234,235,236,237,238,240,241,245,246,251,252,],[80,-29,80,80,-65,-66,-67,-68,-69,-70,-71,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,80,-72,-132,-131,-93,-95,-105,-108,-110,-113,-121,-122,-88,-90,80,80,-132,-73,-57,-115,-116,-94,-132,-132,-132,-132,-120,-89,-91,-92,-128,-56,-132,-59,-132,-75,80,-119,-114,-106,-107,-111,-112,-55,80,80,-58,-74,-124,80,-127,-117,-118,-76,80,-78,80,80,-126,-77,80,-125,]),'WHILE':([53,59,66,67,69,70,71,72,73,74,75,104,105,106,109,111,112,113,114,115,116,117,118,119,120,129,131,132,138,139,141,150,153,154,157,159,160,161,164,173,174,177,178,179,184,187,189,190,191,192,193,194,196,197,198,209,210,211,212,213,214,215,218,219,220,221,222,223,224,225,226,229,230,231,232,233,234,235,236,237,238,240,241,245,246,251,252,],[81,-29,81,81,-65,-66,-67,-68,-69,-70,-71,-132,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,81,-72,-132,-131,-93,-95,-105,-108,-110,-113,-121,-122,-88,-90,81,81,-132,-73,-57,-115,-116,-94,-132,-132,-132,-132,-120,-89,-91,-92,-128,-56,-132,-59,-132,-75,81,-119,-114,-106,-107,-111,-112,-55,81,81,-58,-74,-124,81,-127,-117,-118,-76,81,-78,81,81,-126,-77,81,-125,]),'DOT':([76,120,133,],[98,163,98,]),'EQUALS':([76,96,99,133,182,],[-132,130,-130,-132,-129,]),'SUM':([80,97,100,101,104,105,106,107,109,111,112,113,114,115,116,117,118,119,120,121,130,132,135,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164,180,185,189,190,191,192,193,194,196,197,198,211,213,216,220,221,222,223,224,],[108,108,108,108,-132,151,-109,108,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,108,108,108,-123,-93,108,-95,-96,-97,-98,-99,-100,-101,-102,-103,-105,108,108,-108,-110,108,108,-113,-121,-122,-88,108,-90,108,108,-94,151,151,-132,-132,-120,-89,-91,-92,108,108,-123,-106,-107,-111,-112,-55,]),'SUBTRACT':([80,97,100,101,104,105,106,107,109,111,112,113,114,115,116,117,118,119,120,121,130,132,135,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164,180,185,189,190,191,192,193,194,196,197,198,211,213,216,220,221,222,223,224,],[110,110,110,110,-132,152,-109,110,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,110,110,110,-123,-93,110,-95,-96,-97,-98,-99,-100,-101,-102,-103,-105,110,110,-108,-110,110,110,-113,-121,-122,-88,110,-90,110,110,-94,152,152,-132,-132,-120,-89,-91,-92,110,110,-123,-106,-107,-111,-112,-55,]),'TRUE':([80,97,100,101,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,130,132,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164,180,185,189,190,191,192,193,194,196,197,198,211,213,220,221,222,223,224,],[113,113,113,113,-132,-104,-109,113,113,-123,113,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,113,113,113,-93,113,-95,-96,-97,-98,-99,-100,-101,-102,-103,-105,113,113,-108,-110,113,113,-113,-121,-122,-88,113,-90,113,113,-94,-132,-132,-132,-132,-120,-89,-91,-92,113,113,-106,-107,-111,-112,-55,]),'FALSE':([80,97,100,101,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,130,132,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164,180,185,189,190,191,192,193,194,196,197,198,211,213,220,221,222,223,224,],[114,114,114,114,-132,-104,-109,114,114,-123,114,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,114,114,114,-93,114,-95,-96,-97,-98,-99,-100,-101,-102,-103,-105,114,114,-108,-110,114,114,-113,-121,-122,-88,114,-90,114,114,-94,-132,-132,-132,-132,-120,-89,-91,-92,114,114,-106,-107,-111,-112,-55,]),'CTEFLOAT':([80,97,100,101,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,130,132,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164,180,185,189,190,191,192,193,194,196,197,198,211,213,220,221,222,223,224,],[115,115,115,115,-132,-104,-109,115,115,-123,115,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,115,115,115,-93,115,-95,-96,-97,-98,-99,-100,-101,-102,-103,-105,115,115,-108,-110,115,115,-113,-121,-122,-88,115,-90,115,115,-94,-132,-132,-132,-132,-120,-89,-91,-92,115,115,-106,-107,-111,-112,-55,]),'CTESTRING':([80,97,100,101,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,130,132,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164,180,185,189,190,191,192,193,194,196,197,198,211,213,220,221,222,223,224,],[116,116,116,116,-132,-104,-109,116,116,-123,116,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,116,116,116,-93,116,-95,-96,-97,-98,-99,-100,-101,-102,-103,-105,116,116,-108,-110,116,116,-113,-121,-122,-88,116,-90,116,116,-94,-132,-132,-132,-132,-120,-89,-91,-92,116,116,-106,-107,-111,-112,-55,]),'SAMEAS':([104,105,106,109,111,112,113,114,115,116,117,118,119,120,135,150,153,154,157,159,160,161,164,190,191,192,193,194,196,197,198,216,220,221,222,223,224,],[142,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-105,-108,-110,-113,-121,-122,-88,-90,-132,-132,-132,-132,-120,-89,-91,-92,-123,-106,-107,-111,-112,-55,]),'BIGGERTHAN':([104,105,106,109,111,112,113,114,115,116,117,118,119,120,135,150,153,154,157,159,160,161,164,190,191,192,193,194,196,197,198,216,220,221,222,223,224,],[143,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-105,-108,-110,-113,-121,-122,-88,-90,-132,-132,-132,-132,-120,-89,-91,-92,-123,-106,-107,-111,-112,-55,]),'BIGGEREQUALSTHAN':([104,105,106,109,111,112,113,114,115,116,117,118,119,120,135,150,153,154,157,159,160,161,164,190,191,192,193,194,196,197,198,216,220,221,222,223,224,],[144,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-105,-108,-110,-113,-121,-122,-88,-90,-132,-132,-132,-132,-120,-89,-91,-92,-123,-106,-107,-111,-112,-55,]),'SMALLTHAN':([104,105,106,109,111,112,113,114,115,116,117,118,119,120,135,150,153,154,157,159,160,161,164,190,191,192,193,194,196,197,198,216,220,221,222,223,224,],[145,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-105,-108,-110,-113,-121,-122,-88,-90,-132,-132,-132,-132,-120,-89,-91,-92,-123,-106,-107,-111,-112,-55,]),'SMALLEQUALSTHAN':([104,105,106,109,111,112,113,114,115,116,117,118,119,120,135,150,153,154,157,159,160,161,164,190,191,192,193,194,196,197,198,216,220,221,222,223,224,],[146,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-105,-108,-110,-113,-121,-122,-88,-90,-132,-132,-132,-132,-120,-89,-91,-92,-123,-106,-107,-111,-112,-55,]),'DIFFERENTTHAN':([104,105,106,109,111,112,113,114,115,116,117,118,119,120,135,150,153,154,157,159,160,161,164,190,191,192,193,194,196,197,198,216,220,221,222,223,224,],[147,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-105,-108,-110,-113,-121,-122,-88,-90,-132,-132,-132,-132,-120,-89,-91,-92,-123,-106,-107,-111,-112,-55,]),'AND':([104,105,106,109,111,112,113,114,115,116,117,118,119,120,135,150,153,154,157,159,160,161,164,190,191,192,193,194,196,197,198,216,220,221,222,223,224,],[148,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-105,-108,-110,-113,-121,-122,-88,-90,-132,-132,-132,-132,-120,-89,-91,-92,-123,-106,-107,-111,-112,-55,]),'OR':([104,105,106,109,111,112,113,114,115,116,117,118,119,120,135,150,153,154,157,159,160,161,164,190,191,192,193,194,196,197,198,216,220,221,222,223,224,],[149,-104,-109,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-105,-108,-110,-113,-121,-122,-88,-90,-132,-132,-132,-132,-120,-89,-91,-92,-123,-106,-107,-111,-112,-55,]),'TIMES':([106,109,111,112,113,114,115,116,117,118,119,120,135,159,160,161,164,192,193,194,196,197,198,216,224,],[155,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-121,-122,-88,-90,155,155,-120,-89,-91,-92,-123,-55,]),'DIV':([106,109,111,112,113,114,115,116,117,118,119,120,135,159,160,161,164,192,193,194,196,197,198,216,224,],[156,-123,-79,-80,-81,-82,-83,-84,-85,-86,-87,-132,-123,-121,-122,-88,-90,156,156,-120,-89,-91,-92,-123,-55,]),'ELSE':([231,233,245,],[244,-127,-126,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'save_program':([3,],[4,]),'altprogram':([5,7,8,9,],[6,15,16,17,]),'class':([5,7,8,9,],[7,7,7,7,]),'var':([5,7,8,9,47,53,55,56,66,67,129,173,174,226,240,241,],[8,8,8,8,55,66,55,55,66,66,173,173,173,240,240,240,]),'function':([5,7,8,9,47,55,56,],[9,9,9,9,56,56,56,]),'main':([5,7,8,9,],[10,10,10,10,]),'listids':([12,39,88,203,],[19,49,125,227,]),'save_main':([14,],[22,]),'altclass':([18,],[23,]),'empty':([18,27,28,52,60,76,90,104,105,106,120,123,132,133,162,168,170,177,190,191,192,193,211,213,243,],[25,41,45,64,89,99,128,141,153,157,164,169,179,99,179,169,204,212,153,153,157,157,179,179,128,]),'save_var_name':([20,],[27,]),'save_class':([23,],[30,]),'type':([26,51,63,205,],[32,61,92,228,]),'listidsalty':([27,],[38,]),'altfunc':([28,],[43,]),'params':([28,123,168,],[44,168,168,]),'save_vars':([32,],[48,]),'alt2class':([47,55,56,],[54,82,83,]),'constructor':([47,55,56,],[57,57,57,]),'alt2func':([52,],[62,]),'altmain':([53,66,67,],[65,93,94,]),'estatuto':([53,66,67,129,173,174,215,225,226,232,237,240,241,251,],[67,67,67,174,174,174,232,237,241,232,237,241,241,232,]),'assign':([53,66,67,129,173,174,215,225,226,232,237,240,241,251,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'condition':([53,66,67,129,173,174,215,225,226,232,237,240,241,251,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'write':([53,66,67,129,173,174,215,225,226,232,237,240,241,251,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'read':([53,66,67,129,173,174,215,225,226,232,237,240,241,251,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'return':([53,66,67,129,173,174,215,225,226,232,237,240,241,251,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'voidcall':([53,66,67,129,173,174,215,225,226,232,237,240,241,251,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'while':([53,66,67,129,173,174,215,225,226,232,237,240,241,251,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'save_constructor':([58,],[85,]),'listidsaltz':([60,],[87,]),'save_params':([61,228,],[90,243,]),'save_function':([62,],[91,]),'clear_scope':([68,],[95,]),'assign1':([76,133,],[96,182,]),'expresion':([80,97,100,101,107,121,130,132,162,180,185,211,213,],[103,132,134,136,158,165,176,177,177,213,217,177,177,]),'exp':([80,97,100,101,107,121,130,132,140,162,180,185,211,213,],[104,104,104,104,104,104,104,104,189,104,104,104,104,104,]),'termino':([80,97,100,101,107,121,130,132,140,151,152,162,180,185,211,213,],[105,105,105,105,105,105,105,105,105,190,191,105,105,105,105,105,]),'factor':([80,97,100,101,107,121,130,132,140,151,152,155,156,162,180,185,211,213,],[106,106,106,106,106,106,106,106,106,106,106,192,193,106,106,106,106,106,]),'varcall':([80,97,100,101,107,108,110,121,130,132,140,151,152,155,156,162,180,185,211,213,],[109,109,109,135,109,159,160,109,109,109,109,109,109,109,109,109,109,216,109,109,]),'varcte':([80,97,100,101,107,108,110,121,130,132,140,151,152,155,156,162,180,185,211,213,],[111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,]),'varcomplicated':([80,97,100,101,107,108,110,121,130,132,140,151,152,155,156,162,180,185,211,213,],[112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,]),'varcomp1':([80,97,100,101,107,108,110,121,130,132,140,151,152,155,156,162,163,180,185,211,213,],[118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,197,118,118,118,118,]),'callfunc':([80,97,100,101,107,108,110,121,130,132,140,151,152,155,156,162,163,180,185,211,213,],[119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,198,119,119,119,119,]),'altparams':([90,243,],[126,250,]),'altexpresion':([104,],[139,]),'altexpresion2':([104,],[140,]),'altexp':([105,190,191,],[150,220,221,]),'alttermino':([106,192,193,],[154,222,223,]),'varcomp2':([120,],[161,]),'remove_class_scope':([122,],[166,]),'altconst':([123,168,],[167,201,]),'alt3func':([129,173,174,],[172,206,207,]),'altcall':([132,162,211,213,],[178,195,229,230,]),'altwrite':([135,136,216,217,],[184,187,234,235,]),'varcomp3':([163,],[196,]),'listidsaltp':([170,],[202,]),'remove_function_scope':([175,],[208,]),'alt2call':([177,],[210,]),'altcondition':([215,232,251,],[231,245,252,]),'altwhile':([225,237,],[236,246,]),'alt2const':([226,240,241,],[239,247,248,]),'remove_constructor_scope':([242,],[249,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID save_program SEMICOLON altprogram','program',5,'p_program','QCSAQ_Parser.py',20),
  ('altprogram -> class altprogram','altprogram',2,'p_program','QCSAQ_Parser.py',21),
  ('altprogram -> var altprogram','altprogram',2,'p_program','QCSAQ_Parser.py',22),
  ('altprogram -> function altprogram','altprogram',2,'p_program','QCSAQ_Parser.py',23),
  ('altprogram -> main','altprogram',1,'p_program','QCSAQ_Parser.py',24),
  ('save_program -> <empty>','save_program',0,'p_save_program','QCSAQ_Parser.py',30),
  ('main -> MAIN save_main OPENPAREN CLOSEPAREN OPENCURLY altmain','main',6,'p_main','QCSAQ_Parser.py',37),
  ('altmain -> var altmain','altmain',2,'p_main','QCSAQ_Parser.py',38),
  ('altmain -> estatuto altmain','altmain',2,'p_main','QCSAQ_Parser.py',39),
  ('altmain -> CLOSECURLY clear_scope','altmain',2,'p_main','QCSAQ_Parser.py',40),
  ('save_main -> <empty>','save_main',0,'p_save_main','QCSAQ_Parser.py',46),
  ('clear_scope -> <empty>','clear_scope',0,'p_clear_scope','QCSAQ_Parser.py',53),
  ('class -> CLASS ID altclass save_class OPENCURLY alt2class','class',6,'p_class','QCSAQ_Parser.py',60),
  ('altclass -> TWODOTS ID','altclass',2,'p_class','QCSAQ_Parser.py',61),
  ('altclass -> empty','altclass',1,'p_class','QCSAQ_Parser.py',62),
  ('alt2class -> var alt2class','alt2class',2,'p_class','QCSAQ_Parser.py',63),
  ('alt2class -> function alt2class','alt2class',2,'p_class','QCSAQ_Parser.py',64),
  ('alt2class -> constructor CLOSECURLY SEMICOLON remove_class_scope','alt2class',4,'p_class','QCSAQ_Parser.py',65),
  ('save_class -> <empty>','save_class',0,'p_save_class','QCSAQ_Parser.py',74),
  ('remove_class_scope -> <empty>','remove_class_scope',0,'p_remove_class_scope','QCSAQ_Parser.py',81),
  ('constructor -> CONSTRUCTOR save_constructor OPENPAREN altconst CLOSEPAREN OPENCURLY alt2const','constructor',7,'p_constructor','QCSAQ_Parser.py',87),
  ('altconst -> params altconst','altconst',2,'p_constructor','QCSAQ_Parser.py',88),
  ('altconst -> empty','altconst',1,'p_constructor','QCSAQ_Parser.py',89),
  ('alt2const -> var alt2const','alt2const',2,'p_constructor','QCSAQ_Parser.py',90),
  ('alt2const -> estatuto alt2const','alt2const',2,'p_constructor','QCSAQ_Parser.py',91),
  ('alt2const -> CLOSECURLY remove_constructor_scope','alt2const',2,'p_constructor','QCSAQ_Parser.py',92),
  ('save_constructor -> <empty>','save_constructor',0,'p_save_constructor','QCSAQ_Parser.py',98),
  ('remove_constructor_scope -> <empty>','remove_constructor_scope',0,'p_remove_constructor_scope','QCSAQ_Parser.py',104),
  ('var -> VAR listids TWODOTS type save_vars SEMICOLON','var',6,'p_var','QCSAQ_Parser.py',110),
  ('save_vars -> <empty>','save_vars',0,'p_save_vars','QCSAQ_Parser.py',116),
  ('listids -> ID save_var_name listidsalty','listids',3,'p_listids','QCSAQ_Parser.py',125),
  ('listidsalty -> COMMA listids','listidsalty',2,'p_listids','QCSAQ_Parser.py',126),
  ('listidsalty -> OPENBRACKET CTEINT CLOSEBRACKET listidsaltz','listidsalty',4,'p_listids','QCSAQ_Parser.py',127),
  ('listidsalty -> empty','listidsalty',1,'p_listids','QCSAQ_Parser.py',128),
  ('listidsaltz -> COMMA listids','listidsaltz',2,'p_listids','QCSAQ_Parser.py',129),
  ('listidsaltz -> OPENBRACKET CTEINT CLOSEBRACKET listidsaltp','listidsaltz',4,'p_listids','QCSAQ_Parser.py',130),
  ('listidsaltz -> empty','listidsaltz',1,'p_listids','QCSAQ_Parser.py',131),
  ('listidsaltp -> COMMA listids','listidsaltp',2,'p_listids','QCSAQ_Parser.py',132),
  ('listidsaltp -> empty','listidsaltp',1,'p_listids','QCSAQ_Parser.py',133),
  ('save_var_name -> <empty>','save_var_name',0,'p_save_var_name','QCSAQ_Parser.py',139),
  ('function -> FUNC ID OPENPAREN altfunc CLOSEPAREN alt2func save_function OPENCURLY alt3func','function',9,'p_function','QCSAQ_Parser.py',146),
  ('altfunc -> params','altfunc',1,'p_function','QCSAQ_Parser.py',147),
  ('altfunc -> empty','altfunc',1,'p_function','QCSAQ_Parser.py',148),
  ('alt2func -> TWODOTS type','alt2func',2,'p_function','QCSAQ_Parser.py',149),
  ('alt2func -> empty','alt2func',1,'p_function','QCSAQ_Parser.py',150),
  ('alt3func -> var alt3func','alt3func',2,'p_function','QCSAQ_Parser.py',151),
  ('alt3func -> estatuto alt3func','alt3func',2,'p_function','QCSAQ_Parser.py',152),
  ('alt3func -> CLOSECURLY remove_function_scope','alt3func',2,'p_function','QCSAQ_Parser.py',153),
  ('save_function -> <empty>','save_function',0,'p_save_function','QCSAQ_Parser.py',163),
  ('remove_function_scope -> <empty>','remove_function_scope',0,'p_remove_function_scope','QCSAQ_Parser.py',170),
  ('params -> ID TWODOTS type save_params altparams','params',5,'p_params','QCSAQ_Parser.py',176),
  ('altparams -> COMMA ID TWODOTS type save_params altparams','altparams',6,'p_params','QCSAQ_Parser.py',177),
  ('altparams -> empty','altparams',1,'p_params','QCSAQ_Parser.py',178),
  ('save_params -> <empty>','save_params',0,'p_save_params','QCSAQ_Parser.py',184),
  ('callfunc -> ID OPENPAREN altcall CLOSEPAREN','callfunc',4,'p_callfunc','QCSAQ_Parser.py',191),
  ('altcall -> expresion alt2call','altcall',2,'p_callfunc','QCSAQ_Parser.py',192),
  ('altcall -> empty','altcall',1,'p_callfunc','QCSAQ_Parser.py',193),
  ('alt2call -> COMMA altcall','alt2call',2,'p_callfunc','QCSAQ_Parser.py',194),
  ('alt2call -> empty','alt2call',1,'p_callfunc','QCSAQ_Parser.py',195),
  ('type -> INT','type',1,'p_type','QCSAQ_Parser.py',201),
  ('type -> FLOAT','type',1,'p_type','QCSAQ_Parser.py',202),
  ('type -> STRING','type',1,'p_type','QCSAQ_Parser.py',203),
  ('type -> ID','type',1,'p_type','QCSAQ_Parser.py',204),
  ('type -> BOOL','type',1,'p_type','QCSAQ_Parser.py',205),
  ('estatuto -> assign','estatuto',1,'p_estatuto','QCSAQ_Parser.py',212),
  ('estatuto -> condition','estatuto',1,'p_estatuto','QCSAQ_Parser.py',213),
  ('estatuto -> write','estatuto',1,'p_estatuto','QCSAQ_Parser.py',214),
  ('estatuto -> read','estatuto',1,'p_estatuto','QCSAQ_Parser.py',215),
  ('estatuto -> return','estatuto',1,'p_estatuto','QCSAQ_Parser.py',216),
  ('estatuto -> voidcall','estatuto',1,'p_estatuto','QCSAQ_Parser.py',217),
  ('estatuto -> while','estatuto',1,'p_estatuto','QCSAQ_Parser.py',218),
  ('voidcall -> ID OPENPAREN CLOSEPAREN','voidcall',3,'p_voidcall','QCSAQ_Parser.py',224),
  ('voidcall -> ID OPENPAREN expresion altcall','voidcall',4,'p_voidcall','QCSAQ_Parser.py',225),
  ('altcall -> COMMA expresion altcall','altcall',3,'p_voidcall','QCSAQ_Parser.py',226),
  ('altcall -> CLOSEPAREN SEMICOLON','altcall',2,'p_voidcall','QCSAQ_Parser.py',227),
  ('while -> WHILE OPENPAREN expresion CLOSEPAREN OPENCURLY altwhile','while',6,'p_while','QCSAQ_Parser.py',233),
  ('altwhile -> estatuto altwhile','altwhile',2,'p_while','QCSAQ_Parser.py',234),
  ('altwhile -> CLOSECURLY','altwhile',1,'p_while','QCSAQ_Parser.py',235),
  ('varcall -> varcte','varcall',1,'p_varcall','QCSAQ_Parser.py',241),
  ('varcall -> varcomplicated','varcall',1,'p_varcall','QCSAQ_Parser.py',242),
  ('varcte -> TRUE','varcte',1,'p_varcte','QCSAQ_Parser.py',247),
  ('varcte -> FALSE','varcte',1,'p_varcte','QCSAQ_Parser.py',248),
  ('varcte -> CTEFLOAT','varcte',1,'p_varcte','QCSAQ_Parser.py',249),
  ('varcte -> CTESTRING','varcte',1,'p_varcte','QCSAQ_Parser.py',250),
  ('varcte -> CTEINT','varcte',1,'p_varcte','QCSAQ_Parser.py',251),
  ('varcomplicated -> varcomp1','varcomplicated',1,'p_varcomplicated','QCSAQ_Parser.py',257),
  ('varcomplicated -> callfunc','varcomplicated',1,'p_varcomplicated','QCSAQ_Parser.py',258),
  ('varcomp1 -> ID varcomp2','varcomp1',2,'p_varcomplicated','QCSAQ_Parser.py',259),
  ('varcomp2 -> DOT varcomp3','varcomp2',2,'p_varcomplicated','QCSAQ_Parser.py',260),
  ('varcomp2 -> empty','varcomp2',1,'p_varcomplicated','QCSAQ_Parser.py',261),
  ('varcomp3 -> varcomp1','varcomp3',1,'p_varcomplicated','QCSAQ_Parser.py',262),
  ('varcomp3 -> callfunc','varcomp3',1,'p_varcomplicated','QCSAQ_Parser.py',263),
  ('expresion -> exp altexpresion','expresion',2,'p_expresion','QCSAQ_Parser.py',269),
  ('altexpresion -> altexpresion2 exp','altexpresion',2,'p_expresion','QCSAQ_Parser.py',270),
  ('altexpresion -> empty','altexpresion',1,'p_expresion','QCSAQ_Parser.py',271),
  ('altexpresion2 -> SAMEAS','altexpresion2',1,'p_expresion','QCSAQ_Parser.py',272),
  ('altexpresion2 -> BIGGERTHAN','altexpresion2',1,'p_expresion','QCSAQ_Parser.py',273),
  ('altexpresion2 -> BIGGEREQUALSTHAN','altexpresion2',1,'p_expresion','QCSAQ_Parser.py',274),
  ('altexpresion2 -> SMALLTHAN','altexpresion2',1,'p_expresion','QCSAQ_Parser.py',275),
  ('altexpresion2 -> SMALLEQUALSTHAN','altexpresion2',1,'p_expresion','QCSAQ_Parser.py',276),
  ('altexpresion2 -> DIFFERENTTHAN','altexpresion2',1,'p_expresion','QCSAQ_Parser.py',277),
  ('altexpresion2 -> AND','altexpresion2',1,'p_expresion','QCSAQ_Parser.py',278),
  ('altexpresion2 -> OR','altexpresion2',1,'p_expresion','QCSAQ_Parser.py',279),
  ('exp -> termino','exp',1,'p_exp','QCSAQ_Parser.py',285),
  ('exp -> termino altexp','exp',2,'p_exp','QCSAQ_Parser.py',286),
  ('altexp -> SUM termino altexp','altexp',3,'p_exp','QCSAQ_Parser.py',287),
  ('altexp -> SUBTRACT termino altexp','altexp',3,'p_exp','QCSAQ_Parser.py',288),
  ('altexp -> empty','altexp',1,'p_exp','QCSAQ_Parser.py',289),
  ('termino -> factor','termino',1,'p_termino','QCSAQ_Parser.py',295),
  ('termino -> factor alttermino','termino',2,'p_termino','QCSAQ_Parser.py',296),
  ('alttermino -> TIMES factor alttermino','alttermino',3,'p_termino','QCSAQ_Parser.py',297),
  ('alttermino -> DIV factor alttermino','alttermino',3,'p_termino','QCSAQ_Parser.py',298),
  ('alttermino -> empty','alttermino',1,'p_termino','QCSAQ_Parser.py',299),
  ('read -> INPUT OPENPAREN ID CLOSEPAREN SEMICOLON','read',5,'p_read','QCSAQ_Parser.py',305),
  ('write -> OUTPUT OPENPAREN varcall altwrite','write',4,'p_write','QCSAQ_Parser.py',311),
  ('write -> OUTPUT OPENPAREN expresion altwrite','write',4,'p_write','QCSAQ_Parser.py',312),
  ('altwrite -> COMMA varcall altwrite','altwrite',3,'p_write','QCSAQ_Parser.py',313),
  ('altwrite -> COMMA expresion altwrite','altwrite',3,'p_write','QCSAQ_Parser.py',314),
  ('altwrite -> CLOSEPAREN SEMICOLON','altwrite',2,'p_write','QCSAQ_Parser.py',315),
  ('factor -> OPENPAREN expresion CLOSEPAREN','factor',3,'p_factor','QCSAQ_Parser.py',321),
  ('factor -> SUM varcall','factor',2,'p_factor','QCSAQ_Parser.py',322),
  ('factor -> SUBTRACT varcall','factor',2,'p_factor','QCSAQ_Parser.py',323),
  ('factor -> varcall','factor',1,'p_factor','QCSAQ_Parser.py',324),
  ('condition -> IF OPENPAREN expresion CLOSEPAREN OPENCURLY altcondition','condition',6,'p_condition','QCSAQ_Parser.py',330),
  ('condition -> IF OPENPAREN expresion CLOSEPAREN OPENCURLY altcondition ELSE OPENCURLY altcondition','condition',9,'p_condition','QCSAQ_Parser.py',331),
  ('altcondition -> estatuto altcondition','altcondition',2,'p_condition','QCSAQ_Parser.py',332),
  ('altcondition -> CLOSECURLY','altcondition',1,'p_condition','QCSAQ_Parser.py',333),
  ('assign -> ID assign1 EQUALS expresion SEMICOLON','assign',5,'p_assign','QCSAQ_Parser.py',339),
  ('assign1 -> DOT ID assign1','assign1',3,'p_assign','QCSAQ_Parser.py',340),
  ('assign1 -> empty','assign1',1,'p_assign','QCSAQ_Parser.py',341),
  ('return -> RETURN expresion SEMICOLON','return',3,'p_return','QCSAQ_Parser.py',347),
  ('empty -> <empty>','empty',0,'p_empty','QCSAQ_Parser.py',353),
]
