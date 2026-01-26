/*
Author       : sellerend
Template Name: Directory listing template
Version      : 1.0
*/

(function($) {
	'use strict';
	/*START SWIPER JS*/

	new WOW().init();
	AOS.init();

	// loader
	$(window).on( "load", function() {
		$('.preloader').fadeOut(1000);
	});

	// nice select

	$("#homeTwoCategory").niceSelect()
	$("#location").niceSelect()
	$("#category").niceSelect()
	$(".listing_select").niceSelect()


	new Swiper(".category_swipper", {
		slidesPerView: 5,
		spaceBetween: 30,
		speed: 1000,
		navigation: {
		  nextEl: ".swiper-button-next",
		  prevEl: ".swiper-button-prev",
		},
		loop: true,
		breakpoints: {
			1200: {
				slidesPerView: 5,
			},
			1199: {
				slidesPerView: 4,
			}, 
			767: {
				slidesPerView: 2,
			}, 
			320: {
				slidesPerView: 1,
			}, 
		},
	});
 
	  
	/*END SWIPER JS*/	

	var fixed_top = $("#menu_section");
	$(window).on('scroll', function () {
		if ($(this).scrollTop() > 200) {
			fixed_top.addClass("sticky-menu animated fadeInDown");
		} else {
			fixed_top.removeClass("sticky-menu animated fadeInDown");
		}
	});

	$(window).on('scroll', function () {
		if ($(this).scrollTop() > 300) {
			$('.scrollToTop').css({
				'bottom': '2%',
				'opacity': '1',
				'transition': 'all .5s ease'
			});
		} else {
			$('.scrollToTop').css({
				'bottom': '-30%',
				'opacity': '0',
				'transition': 'all .5s ease'
			})
		}
	});

	//Click event to scroll to top
	$('a.scrollToTop').on('click', function () {
		$('html, body').animate({
			scrollTop: 0
		}, 500);
		return false;
	});
	 

	$(document).ready(function(){
		$(".mobile_menu_top_right span").click(function(){
		$(".mobile_menu_top_right").toggleClass("close");
			$(".mobile_menu_bottom").toggleClass("open");
		});
	});
		
	$(".main_mobile_menu ul li ul").parent("li").addClass("mobile_drowpdown");
	$('.main_mobile_menu ul li a').on('click', function(e) {
		var element = $(this).parent('li');
		if (element.hasClass('open')) {
			element.removeClass('open');
			element.find('li').removeClass('open');
			element.find('ul').slideUp("swing");
		}
		else {
			element.addClass('open');
			element.children('ul').slideDown("swing");
			element.siblings('li').children('ul').slideUp("swing");
			element.siblings('li').removeClass('open');
			element.siblings('li').find('li').removeClass('open');
			element.siblings('li').find('ul').slideUp("swing");
		}
	});		


})(jQuery);


