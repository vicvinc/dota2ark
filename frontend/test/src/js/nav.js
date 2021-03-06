/* 
* @Author: Administrator
* @Date:   2015-08-12 17:08:16
* @Last Modified by:   Administrator
* @Last Modified time: 2015-08-27 09:59:35
*/

'use strict';

require('../../dist/css/main.css');
require('../../dist/css/nav.css');

var nav = {}

nav.item = [
	{
		'mu': 'home',
		'href': '/home',
		'dis': '首页'
	},{
		'mu': 'news',
		'href': '/news',
		'dis': '新闻'
	},{
		'mu': 'forum',
		'href': '/forum',
		'dis': '社区'
	}
]

nav.view = function (ctrl) {
	return m('nav#navigation',[
				m('div#navContainer', 
					nav.item.map(function(item){
						return m('a#navMenu',{href: item.href}, item.dis);
					}))
			]);
};
var navBar = document.getElementById('navx');
m.module(navBar, nav);
