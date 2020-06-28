grammar job;


// Description scope not implemented

// The idea of commenting one block by simply adding a special char to comment that block not implemented
// @scope_name {
//    .....
//  }


job : (configuration_scopes | style |  project_name )*;

configuration_scopes :  project_source_scope |  build_triggers_scope  |  building_scope ;

style : 'style' ('free' | 'maven');
project_name : 'project_name' (Identifier)+;
project_source_scope : 'source' '{' project_source_op* '}';

project_source_op : ( Project_url Identifier+) |
( Git_repo_urls Identifier+) |
(Git_repo_branches (Identifier+)) |
( Credential_name Identifier+);


Project_url : 'project_url';
Git_repo_urls : 'git_repo_urls';
Git_repo_branches : 'git_repo_branches';
Credential_name : 'credential_name';


build_triggers_scope : 'build_triggers' '{' (triggers)* '}';

triggers : poll_scm |build_priodically| build_after_other_projects  ;
poll_scm :  'poll_scm' '{'  ( pattern*  ( Ignore_post_commit_hooks  (Yes | No))? pattern* )  '}';
build_after_other_projects :  'build_after_other_projects' '{' (((Trigger_method DIGIT) (Project_names Identifier+)) | ( (Project_names Identifier+) (Trigger_method DIGIT)))? '}';
build_priodically :   'build_periodically' '{' pattern* '}';

Trigger_method: 'trigger_method'; // for build_after_other_projects
Project_names: 'project_names';  // for build_after_other_projects


Ignore_post_commit_hooks : 'ignore_post_commit_hooks';
Yes : 'yes';
No : 'no';

pattern:  'p-' ( DIGIT | '*')  ( DIGIT | '*') ( DIGIT | '*') ( DIGIT | '*') ( DIGIT | '*');


building_scope: 'building'  '{' (build_directives)* '}';

build_directives :  (shell_command |  (goals_option) |  (root_pom) | (post_step) );

shell_command: 'sh-'  (Identifier)+;
goals_option : 'goals_options' (Identifier)+;
root_pom: 'root_pom' (Identifier)+;
post_step : 'post_step' ('run_if_build_succeed' | 'run_if_build_succeed_unstable' | 'run_regardless' );


DIGIT: [0-9];

Identifier: ('\'')? ([a-zA-Z_0-9]  | '/' | ':' | '.' | '\'' )+ ('\'')?;

COMMENT : ('#') ~('\n')* -> channel(HIDDEN);

BlockComment
    : ('/*' .*? '*/' ) -> skip;
WS:[ \t\r\n]+->skip;
