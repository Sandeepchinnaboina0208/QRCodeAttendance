from django.shortcuts import render
import qrcode
from django.http import HttpResponse, HttpResponseRedirect
from io import BytesIO
def qrcodegeneration(request):
    return render(request, 'Attandance/qrcodegeneration.html')



def generate_qr_code(request):
    # Data to encode in the QR code
    data = "https://yourwebsite.com/user-profile"  # Replace with dynamic data if needed

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Convert to HTTP response
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return HttpResponse(buffer.getvalue(), content_type="image/png")

def studentattendance(request):
    if request.method == "POST":
        # Process the attendance data
        # e.g., save the attendance status for each student in the database
        # Redirect to a success page or back to the attendance page
        return HttpResponseRedirect('/attendance-success/')

    # Render the attendance page
    return render(request, 'Attandance/attandance.html')

def submit_attendance(request):
    return render(request,'Attandance/Attandancesuccess.html')
