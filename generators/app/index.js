var Generator = require('yeoman-generator')
function promise( fn, str ){
  return new Promise(( resolve, reject )=>{
    resolve( fn( str ));
  })
}
function unspace( str="" ){
  return str.replace(/ /g, '');
}
function lower( w="" ){
  return w.toLowerCase();
}
function slugify( str="" ){
  if( !str.includes(' ')) return lower( str );
  return str.split(' ').map( lower ).join('-');
}
function capitalize( str="", forcelower ){
  let start=str[0].toUpperCase();
  let end=str.slice(1);
  if( forcelower ) end=lower( end );
  return start+end;
}
function unslug( str="" ){
  str=str.replace(/ /g, '');
  if( str.includes('-')){
    return str.split('-').map( s=>capitalize( s, true )).join('');
  }
  return str;
}

class Base extends Generator{
  constructor( args, opt ){
    super( args, opt );
    this.props={};
  }
  copyTpl( tpl, dest ){
    this.fs.copyTpl(
      this.templatePath(tpl),
      this.destinationPath( dest || tpl ),
      this.props
    );
  }
}

module.exports=class extends Base{
  prompting(){
    let prompts=[
      {
        type: 'input',
        name: 'title',
        message: 'Title of your project'
      }
    ];
    return this.prompt( prompts ).then( props=>{
      this.props=Object.assign({}, this.props, props );
    });
  }
  writing(){
    this.fs.copyTpl(
      this.templatePath("**/*"),
      this.destinationPath(),
      this.props );
  }
}
