var MyCollect = function () {
};

MyCollect.prototype.listenDeleteCollect = function () {
    $(".delete-collect-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var collect_id = $this.attr('collect-id');

        $.ajax({
            url: "/delete_collect/",
            type: 'POST',
            data: {
                collect_id
            },
            success: function (result) {
                if (result['code'] === 200) {
                    alert('删除成功');
                    location.reload()
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};

MyCollect.prototype.run = function () {
    this.listenDeleteCollect();
};


$(function () {
    var handler = new MyCollect();
    handler.run();
});