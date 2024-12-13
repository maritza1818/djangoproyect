import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { DiscotecaService } from '../../app/core/services/discoteca.service';

@Component({
  selector: 'app-upload-image',
  templateUrl: './upload-image.component.html',
})
export class UploadImageComponent {
  imageUrl: string = '';

  constructor(private http: HttpClient, private discotecaService: DiscotecaService) {}

  uploadImage(event: any) {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('upload_preset', 'my_disco');  
    formData.append('folder', 'mi_discoteca/images');
    const cloudinaryUrl = `https://api.cloudinary.com/v1_1/dz6slezpq/image/upload`;

    this.http.post<any>(cloudinaryUrl, formData)
      .subscribe(response => {
        this.imageUrl = response.secure_url;
      });
  }

  createDiscoteca() {
    const discotecaData = {
      nombre: 'Discoteca Ejemplo',
      direccion: 'Dirección Ejemplo',
      imagen: this.imageUrl,
    };

    this.discotecaService.createDiscoteca(discotecaData).subscribe(response => {
      console.log('Discoteca creada:', response);
    });
  }
}
