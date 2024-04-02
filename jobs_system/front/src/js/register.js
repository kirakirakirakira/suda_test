var Register = function () {
};

Register.prototype.listenSubmitEvent = function () {
    $("#submit-btn").on("click", function (event) {
        event.preventDefault();
        var username = $("#username").val();
        var password1 = $("#password1").val();
        var password2 = $("#password2").val();
        var phone = $("#input-phone").val();

        $.ajax({
            url: "/register/",
            type: 'POST',
            data: {
                username,
                password1,
                password2,
                phone,
            },
            success: function (result) {
                if (result['code'] === 200) {
                    alert('注册成功');
                    window.location = "/login"
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};

Register.prototype.run = function () {
    this.listenSubmitEvent();
};


$(function () {
    var handler = new Register();
    handler.run();
});