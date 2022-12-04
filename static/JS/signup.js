$(document).ready(function () {
    $('.rankimage').each(function (){
            let num = ($(this).attr('id'));
            $(this).attr('src', images[num]);
    })

    $('.agentimage').each(function (){
            let num = ($(this).attr('id'));
            $(this).attr('src', agentsimages[num - 1]);
    })
})