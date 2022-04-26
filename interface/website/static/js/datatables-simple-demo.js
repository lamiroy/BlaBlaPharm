window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        var All = 160
        new simpleDatatables.DataTable(datatablesSimple,{
            perPageSelect: [10, 25, All],
            perPage:10
        });
    }

    const datatablesExpr = document.getElementById('datatablesExpr');
    if (datatablesExpr) {
        new simpleDatatables.DataTable(datatablesExpr,{
            perPageSelect: [10, 25, 60],
            perPage:10
        });
    }
});
