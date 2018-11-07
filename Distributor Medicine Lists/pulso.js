var Excel = require('exceljs');

var workbook = new Excel.Workbook();
workbook.xlsx.readFile("PULSO ITEM LIST_RAW FORMAT.xlsx")
    .then(function() {
        var worksheet = workbook.getWorksheet('Sheet1');
        worksheet.eachRow(function(row,rowNumber) {
            // console.log(rowNumber);
            var description = row.values[2];
            var packaging = row.values[3];
            try{

                description = description.toUpperCase();
                var pkg = packaging.replace(" ","").replace("'","").replace("1VIAL","").replace("VIAL","").replace("EACH","").replace("MD","")
                des = description.replace(/\.*$/,"").replace("CAPS","").replace("CAP'S","").replace("CAP","").replace("TAB","").replace("OINT","OINTMENT").replace("(","").replace(")","").replace("mg","MG").replace(" MG","MG").replace(" GM","GM").replace(/\d+GMS/,"").replace(/\d+GM/,"").replace("VIAL","").replace("LIQ","").replace("SMALL","").replace("SUSP","SUSPENSION").replace("SYP","SYRUP").replace("EXPT","EXPECTORANT").replace("SOLU","SOLUTION").replace("INJ","INJECTION");
                des = des + " " + pkg
                console.log(des);

            }
            catch(err){
                // console.log(err);
                var des = description.replace(/\.$/,"").replace("CAPS","").replace("CAP'S","").replace("CAP","").replace("TAB","").replace("OINT","OINTMENT").replace("(","").replace(")","").replace("mg","MG").replace(" MG","MG").replace(/\d+GMS/,"").replace(/\d+GM/,"").replace("VIAL","").replace("LIQ","").replace("SMALL","").replace("SUSP","SUSPENSION").replace("SYP","SYRUP").replace("EXPT","EXPECTORANT").replace("SOLU","SOLUTION").replace("INJ","INJECTION");
                console.log(des);
            }

        });
});
