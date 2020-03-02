
var Menu = new Class({

	Implements: Options,
	
	initialize: function(el, options){
		this.setOptions(options);
		el = $(el);
		
		var lis = el.getElements('li'), 
		uls = [], 
		ti = 0,
		ul;
		
		this.isH = el.getElement('ul').addClass('menuh');
		
		lis.each(function(li){
			
			/*pour rendre compatible la navigation via la tabulation, a voir de la réèlle nécessité, je suis pas super au courant des tecnhique d'accessibilité*/
			li.setAttribute('tabIndex', ti++);
			li.getElement('a').setAttribute('tabIndex', ti++);
		
			if(ul = li.getElement('ul')){
				li.ul = ul;
				
				uls.push(ul);
				
				li.show = new Fx.Morph(ul, {
					duration : this.options.ulAnim.duration,
					transition : this.options.ulAnim.transition
				});
				
				ul.setStyles({visibility : 'hidden', display : 'block'});
				li.stepsOpen = this.getPropertiesSteps(ul, this.options.ulAnim.startStyles);
			}
			
			li.hide = this.hide.bind(this, li);
			li.addEvent('mouseleave', this.hideTimeout.bind(this, li));
			li.addEvent('mouseenter', this.enter.bind(this, li));
			li.addEvent('focus', this.hideTimeout.bind(this, li));
			li.addEvent('blur', this.enter.bind(this, li));
			
			if(!this.options.liAnim.notInBar || li.parentNode.parentNode != el){
				
				li.enter = new Fx.Morph(li, {
					duration : this.options.liAnim.duration,
					transition : this.options.liAnim.transition
				});
				
				li.steps = this.getPropertiesSteps(li, this.options.liAnim.endStyles, true);
				
				li.enter.start(li.steps[0]);//bug mootools, sans doute d'initialisation , donc on lance l'anime dans le 'vide' ..
				
			}else li.addCls = true;
			
		}, this)
		
		uls.each(function(ul){
			ul.setStyles({display : 'none', visibility : 'visible'});
		});
		
	},
	
	options : {
		ulAnim : {
			delay : 0,
			duration : 600,
			transition : Fx.Transitions.Cubic.easeOut,
			startStyles : {},
			inverseOnHide : true
		},
		liAnim : {
			delay : 0,
			duration : 300,
			transition : Fx.Transitions.Cubic.easeOut,
			startStyles : {},
			inverseOnHide : true
		}
	},
	
	addCls : function(li){
		if(li.addCls || !this.isH){
			li.addClass('lihover');
		}else li.addClass('lilihover');
	},
	
	leave : function(li){
		if(li.parentNode.currentLi == li)
			li.parentNode.currentLi = null;
			
		if(!li.enter || !this.isH){
			li.removeClass('lihover');
		}else li.removeClass('lilihover');
		
		if(li.enter){
			li.enter.cancel();
			li.setStyles(li.steps[0]);
		}
	},
	
	enter : function(li){
		if(li.timeout){
			clearTimeout(li.timeout);
			li.timeout = null;
		}
		
		var pil;
		if(pil = li.parentNode.currentLi){
			if(pil == li)
				return;
			this.leave(pil);
		}
		
		li.parentNode.currentLi = li;
		
		if(li.addCls)
			this.addCls(li);
			
		if(li.enter)
			li.enter.start(li.steps[2]);
		
		
		if(li.ul && li.open)
			return;
		
		if(this.current && this.current != li && this.current != li.parentNode.parentNode){
			var pli = this.current;
			
			do{
				clearTimeout(pli.timeout);
				pli.timeout = null;
				this.hide(pli);
			}while(pli.parentNode != li.parentNode &&  (pli = pli.parentNode.parentNode)  && pli.tagName == 'LI'  );
		}
		
		this.current = li;
		
		if(!li.ul)return;
		
		li.open = true;
		
		li.ul.setStyles(li.stepsOpen[0]);
		li.ul.setStyles({
			display : 'block', 
			overflow : 'hidden',
			'z-index': 5000
		});
		
		li.parentNode.style.overflow = 'visible';
		li.show.start(li.stepsOpen[2]);
	},
	
	hide : function(li){
		this.leave(li);
		
		if(!li.ul)return;
		
		li.open = false;
		li.timeout = null;
		li.ul.setStyles({'display': 'none', 'z-index': 1});
	},
	
	hideTimeout : function(li){	
		this.addCls(li);
		
		li.timeout = setTimeout(li.hide, this.options.ulAnim.delay);
	},
	
	getPropertiesSteps : function(node, startProps, li){
		var i = 0,
		res = [{},{},{}], 
		prop;
		
		for(var i in startProps){
			var step1 = startProps[i],
			step2 = i == 'height' || i == 'width' ? node.getSize()[i == 'width' ? 'x' : 'y'] : node.getStyle(i);
			res[0][i] = li ? step2 : step1;
			res[1][i] = li ? step1 : step2;
			res[2][i] = li ? [step2, step1] : [step1, step2];
		}
		return res;
	}
});