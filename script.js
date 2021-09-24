$(document).ready(
    function()
    {
        $('.menu').hide()
        $('.menu-toggle').click(
            ()=>
            {
                console.log("click")
                // $('.menu').hide()
                   
                $('.menu').slideToggle(200)
            }
        
        
        )
        $('.slide').hide()
        slider()
        var i=0;
        $('.slide').eq($('.slide').length-1).show(1000)

        function slider (){
            $('.slide').hide(1000)
            $('.slide').eq(i).show(1000)
            i++;
            if(i>$('.slide').length)
            {
                $('.slide').eq(0).show(1000)
                i=1
            }
            
            setTimeout(slider,3000)
    }
}
)