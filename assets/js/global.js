 //  Datepicker

 var now = Date.now();
 $(function () {
        $("#expiration_date").datepicker({
            format: 'YYYY-MM-DD',
            startDate: now,
        });
    });