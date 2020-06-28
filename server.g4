grammar server;



serverconf: ( addressrule| portrule)* ;

addressrule : ('Address' | 'address' )    DirectiveValue ;

portrule :  ('Port'|'port')  DirectiveValue;


DirectiveValue: ('\'')? ([0-9] | '.'  )+ ('\'')?;

COMMENT : ('#') ~('\n')* -> channel(HIDDEN);

BlockComment
    : ('/*' .*? '*/' ) -> skip;
WS:[ \t\r\n]+->skip;

ERROR: .;