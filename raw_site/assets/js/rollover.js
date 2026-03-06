
$(function(){
	$(".over").hover(
		function(){
			var activeImg = $(this).attr("src").replace("_off","_on");
			$(this).attr("src",activeImg);
		},
		function(){
			var staticImg = $(this).attr("src").replace("_on","_off");
			$(this).attr("src",staticImg);
		}
	);
});
