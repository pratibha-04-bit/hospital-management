// for department
$(document).ready(function(){
    $('#save').on('click',function(){
        alert('hi department page')
        $deptno = $('#deptno').val();
        $dname = $('#dname').val();
            $.ajax({
                url:'create_dept',
                type:'POST',
                data:{
                    deptno : $deptno,
                    dname  : $dname,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

                },
                success:function(data){
                    alert("created successfully")
                    location.reload()
       
                }
            });
    });

});


//to save doctor detail
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
        // var image_upload = $('input[type=file]').val();
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
                    // image_upload:image_upload,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

                },
                success:function(data){
                    alert('success')
                    location.reload()
                    
                    
                }
            });
    });

    
});
 
//show data in modal
function showFun(e){
    alert('hey')
    var user_id = e.id;
    alert(user_id)
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
    
   //modal update detail
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

//delete doctor detail
$(document).on('click', '#delete', function(){
    alert('delete')
    $id = $(this).attr('name');
    $.ajax({
        url: 'delete/' + $id,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            if (data === 'True') {
                alert('Details deleted successfully!')
                location.reload()
            }

        }
    });
});

//save leave form
$('#save4').on('click',function(){
    alert('leave form')
    var doctor_no = $("#doctor_no").val();
    // var available = $('#available').val();
    var doctor = $("#doctor").val();
    var dept_list =$("[name='dept_list']").val();
    var date = $("#date").val();

    $.ajax({
        url:"save_leave",
        type:'POST',
        data:{
            doctor_no:doctor_no,
            // available:available,
            doctor:doctor,
            dept_list:dept_list,
            date:date,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            alert("successfully inseretd")
            location.reload()
        }

    })
    

});




function showModal(e){
    var data_id = e.id;
    alert(data_id)
    $.ajax({
        url:"leave_modal/"+data_id,
        type:"POST",
        data:{id: data_id,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    },
    success:function(data){
        console.log(data);
        if (data.length > 0) {
            let id = data[0].pk;
            data = data[0].fields;
                $('#doctor_no').val(data.doctor_no);
                $('#doctor_name').val(data.doctor_name);
                $('#department').val(data.department);

                $('#date').val(data.date);
                $('#status').val(data.status);
               
                $('#id').val(id);
                $("#exampleModal").modal('show');
        }
    }
});
}

//check page for update
$('#update_leave').on('click',function(){
    alert('Are you sure, you want to update.?');
    var doctor_no=$('#doctor_no').val();
    var doctor_name =$('#doctor_name').val();
    var department= $('#department').val();
    var date = $('#date').val();
    var status =$("[name='status']").val();
    // var status = $('#status').val();
    var id=$('#id').val();
    let input={
        id:id,
        doctor_no:doctor_no,
        doctor_name:doctor_name,
        department:department,
        date:date,
        status:status
        
    }
    $.ajax({
        url:'check_update',
        type:'POST',
        data: input,
        success:function(data){
            if (data === 'True') {
                alert('Details updated successfully!')
                location.reload()
            }

        }
    });

})



//dependent dropdown
$(document).ready(function(){
    $("#department").change(function(){
      alert($(this).find(':selected').val());
      let dpId = $(this).find(':selected').val();
      $.ajax({
        url:'get_doctors/'+dpId,
        type:'GET',
        success:function(data){

            console.log(data);
            $("#doctor").html("");
            $("#doctor").append(new Option("Choose doctor..", ''));
            for (let i=0; i < data.length; i++) {
                let obj = data[i];
                $("#doctor").append(new Option(obj.fields.doc_name, obj.pk));
            }
            

          

        }
    });

      
    });
})




$("#save_appoint").click(function(e){
    // var data = {
    //     patient_name: $("#patient_name").val(),
    //     age: $("#age").val(),
    //     doctor_id:  $("#doctor").val(),
    //     date:  $("#appointment_date").val(),
    //     gender: $('input[type="radio"]:checked').val()

    // }
    // console.log(data);
    e.preventDefault(e);
        alert('appointments')
        var patient_name= $("#patient_name").val();
        var age=$("#age").val();
        var department=$("#department").val()
        var doctor=$("#doctor").val();
        var appointment_date=$("#appointment_date").val();
        var gender=$('input[type="radio"]:checked').val()

        $.ajax({
            url:'appointment_save',
            type:'POST',
            data:{
                patient_name:patient_name,
                age:age,
                department:department,
                doctor:doctor,
                
                appointment_date:appointment_date,
                gender:gender

            },success: function(data){
                if(data === "True") {
                    alert('success')
                   location.reload();
                } else {
                    alert('Sorry, the the limit reached for this date!')
                }
               // alert('success')
                //window.location.href = "/show"
            }
        })

    
})

