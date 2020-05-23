/*
 * @Author: your name
 * @Date: 2020-05-23 10:19:13
 * @LastEditTime: 2020-05-23 15:40:16
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \sayhello\sayhello\static\js\script.js
 */ 
$(function(){
    function render_time() {
        return moment($(this).data('timestamp')).format('lll')
    }
    $('[data-toggle="tooltip"]').tooltip(
        {title: render_time}
    )
})