 //  Datepicker

 var now = Date.now();
 $(function () {
        $("#id_expiration_date").datepicker({
            format: 'YYYY-MM-DD',
            startDate: now,
        });
    });