+function(t){"use strict";function n(){var t=document.createElement("bootstrap"),n={WebkitTransition:"webkitTransitionEnd",MozTransition:"transitionend",OTransition:"oTransitionEnd otransitionend",transition:"transitionend"};for(var e in n)if(void 0!==t.style[e])return{end:n[e]};return!1}t.fn.emulateTransitionEnd=function(n){var e=!1,i=this;t(this).one("bsTransitionEnd",function(){e=!0});var s=function(){e||t(i).trigger(t.support.transition.end)};return setTimeout(s,n),this},t(function(){t.support.transition=n(),t.support.transition&&(t.event.special.bsTransitionEnd={bindType:t.support.transition.end,delegateType:t.support.transition.end,handle:function(n){return t(n.target).is(this)?n.handleObj.handler.apply(this,arguments):void 0}})})}(jQuery),+function(t){"use strict";function n(n){return this.each(function(){var i=t(this),s=i.data("bs.collapse"),a=t.extend({},e.DEFAULTS,i.data(),"object"==typeof n&&n);!s&&a.toggle&&"show"==n&&(n=!n),s||i.data("bs.collapse",s=new e(this,a)),"string"==typeof n&&s[n]()})}var e=function(n,i){this.$element=t(n),this.options=t.extend({},e.DEFAULTS,i),this.transitioning=null,this.options.parent&&(this.$parent=t(this.options.parent)),this.options.toggle&&this.toggle()};e.VERSION="3.2.0",e.DEFAULTS={toggle:!0},e.prototype.dimension=function(){var t=this.$element.hasClass("width");return t?"width":"height"},e.prototype.show=function(){if(!this.transitioning&&!this.$element.hasClass("in")){var e=t.Event("show.bs.collapse");if(this.$element.trigger(e),!e.isDefaultPrevented()){var i=this.$parent&&this.$parent.find("> .panel > .in");if(i&&i.length){var s=i.data("bs.collapse");if(s&&s.transitioning)return;n.call(i,"hide"),s||i.data("bs.collapse",null)}var a=this.dimension();this.$element.removeClass("collapse").addClass("collapsing")[a](0),this.transitioning=1;var o=function(){this.$element.removeClass("collapsing").addClass("collapse in")[a](""),this.transitioning=0,this.$element.trigger("shown.bs.collapse")};if(!t.support.transition)return o.call(this);var l=t.camelCase(["scroll",a].join("-"));this.$element.one("bsTransitionEnd",t.proxy(o,this)).emulateTransitionEnd(350)[a](this.$element[0][l])}}},e.prototype.hide=function(){if(!this.transitioning&&this.$element.hasClass("in")){var n=t.Event("hide.bs.collapse");if(this.$element.trigger(n),!n.isDefaultPrevented()){var e=this.dimension();this.$element[e](this.$element[e]())[0].offsetHeight,this.$element.addClass("collapsing").removeClass("collapse").removeClass("in"),this.transitioning=1;var i=function(){this.transitioning=0,this.$element.trigger("hidden.bs.collapse").removeClass("collapsing").addClass("collapse")};return t.support.transition?void this.$element[e](0).one("bsTransitionEnd",t.proxy(i,this)).emulateTransitionEnd(350):i.call(this)}}},e.prototype.toggle=function(){this[this.$element.hasClass("in")?"hide":"show"]()};var i=t.fn.collapse;t.fn.collapse=n,t.fn.collapse.Constructor=e,t.fn.collapse.noConflict=function(){return t.fn.collapse=i,this},t(document).on("click.bs.collapse.data-api",'[data-toggle="collapse"]',function(e){var i,s=t(this),a=s.attr("data-target")||e.preventDefault()||(i=s.attr("href"))&&i.replace(/.*(?=#[^\s]+$)/,""),o=t(a),l=o.data("bs.collapse"),r=l?"toggle":s.data(),h=s.attr("data-parent"),p=h&&t(h);l&&l.transitioning||(p&&p.find('[data-toggle="collapse"][data-parent="'+h+'"]').not(s).addClass("collapsed"),s[o.hasClass("in")?"addClass":"removeClass"]("collapsed")),n.call(o,r)})}(jQuery);