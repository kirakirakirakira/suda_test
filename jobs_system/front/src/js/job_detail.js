var JobDetail = function () {
};


JobDetail.prototype.listenScoreEvent = function () {
    $("#score-btn").on("click", function (event) {
        event.preventDefault();
        var score = $("#input-score").val();
        var $this = $(this);
        var job_id = $this.attr('job-id');

        $.ajax({
            url: "/input_score/",
            type: 'POST',
            data: {
                score,
                job_id
            },
            success: function (result) {
                if (result['code'] === 200) {
                    alert('评价成功');
                    location.reload();
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};

JobDetail.prototype.listenAddCollect = function () {
    $("#add-collect-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var job_id = $this.attr('job-id');

        $.ajax({
            url: "/add_collect/",
            type: 'POST',
            data: {
                job_id
            },
            success: function (result) {
                if (result['code'] === 200) {
                    alert('收藏成功');
                    location.reload()
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};


JobDetail.prototype.listenAddOrder = function () {
    $("#add-order-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var job_id = $this.attr('job-id');

        $.ajax({
            url: "/add_order/",
            type: 'POST',
            data: {
                job_id
            },
            success: function (result) {
                if (result['code'] === 200) {
                    alert('投递成功');
                    location.reload()
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};

JobDetail.prototype.listenAddComment = function () {
    $("#add-comment-btn").on("click", function (event) {
        event.preventDefault();
        var $this = $(this);
        var job_id = $this.attr('job-id');
        var content = $('#comment-textarea').val();
        $.ajax({
            url: "/add_comment/",
            type: 'POST',
            data: {
                job_id,
                content
            },
            success: function (result) {
                if (result['code'] === 200) {
                    alert('发布成功');
                    location.reload()
                } else {
                    alert(result['message']);
                }
            }
        })
    });
};


JobDetail.prototype.run = function () {
    this.listenAddCollect();
    this.listenAddOrder();
    this.listenAddComment();
    this.listenScoreEvent();
};


$(function () {
    var handler = new JobDetail();
    handler.run();
});