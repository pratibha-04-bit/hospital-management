$(document).ready(function(){
    $('#save').on('click',function(){
        alert('hii')
        $deptno = $('#deptno').val();
        $dname = $('#dname').val();
            $.ajax({
                url:'create_dept',
                type:'POST',
                data:{
                    deptno : $deptno,
                    dname : $dname,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

                },
                success:function(data){
                    alert('success')
                    window.location.href="/show_dept";
                    
                    
                }
            });
    });

});
//  Doctor page
$(document).ready(function(){
    $('#save1').on('click',function(){
        alert('hello')
        var doc_no = $('#doc_no').val();
        var doc_name = $('#doc_name').val();
        var doc_phone = $('#doc_phone').val();
        var doc_email = $('#doc_email').val();
        var department_id =$("[name='dept']").val();
        var doj =$('#doj').val();
        var gender =$('input[type="radio"]:checked').val();
            alert(gender);
            $.ajax({
                url:'doctor_create',
                type:'POST',
                data:{
                    doc_no:doc_no,
                    doc_name:doc_name, 
                    doc_phone:doc_phone, 
                    doc_email:doc_email,
                    department_id:department_id, 
                    doj:doj,
                    gender:gender,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

                },
                success:function(data){
                    alert('success')
                    location.reload()
                    
                    
                }
            });
    });

    
});




function showFun(e){
    var user_id = e.id;
    alert(user_id)
   // window.location = "doctor_modal/"+user_id;
    $.ajax({
        url:"doctor_modal/"+user_id,
        type:"POST",
        data:{id: user_id,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    },
        success:function(data){
            console.log(data);
            if (data.length > 0) {
                let id = data[0].pk;
                data = data[0].fields;
                    $('#doc_no').val(data.doc_no);
                    $('#doc_name').val(data.doc_name);
                    $('#doc_phone').val(data.doc_phone);
                    $('#doc_email').val(data.doc_email);
                    $('#dept').val(data.dname);
                    $('#doj').val(data.doj);
                    $('#gender').val(data.gender);
                    $('#id').val(id);
                    $("#exampleModalLong").modal('show');
            }
        }
    });
   }

$('#save2').on('click',function(){
    alert('Are you sure, you want to update.?');
    var doc_no = $('#doc_no').val();
    var doc_name = $('#doc_name').val();
    var doc_phone = $('#doc_phone').val();
    var doc_email = $('#doc_email').val();
    var dept =$('#dept').val();
    var doj =$('#doj').val();
    var gender =$('#gender').val();
    var id =$('#id').val();
    let input = {
        id:id,
        doc_no:doc_no,
        doc_name:doc_name, 
        doc_phone:doc_phone, 
        doc_email:doc_email,
        dept:dept, 
        doj:doj,
        gender:gender,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

    }
        $.ajax({
            url:'doctor_update',
            type:'POST',
            data: input,
            success:function(data){
                if (data === 'True') {
                    alert('Details updated successfully!')
                    location.reload()
                }

            }
        });

});

