var MyInfo = function () {
};

MyInfo.prototype.listenSubmitEvent = function () {
    $("#submit-btn").on("click", function (event) {
        event.preventDefault();
        var username = $("#username").val();
        var password = $("#password").val();
        var phone = $("#phone").val();
        var edu_level = $("#edu_level").val();
        var major = $("#major").val();
        var age = $("#age").val();
        var content = $("#my_content").val();
        $.ajax({
            url: "/my_info/",
            type: 'POST',
            data: {
                username,
                password,
                phone,
                edu_level,
                major,
                age,
                content,
            },
            success: function (result) {
                if (result['code'] === 200) {
                    alert('提交成功');
                    location.reload();
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};

MyInfo.prototype.run = function () {
    this.listenSubmitEvent();
};


$(function () {
    var handler = new MyInfo();
    handler.run();
});