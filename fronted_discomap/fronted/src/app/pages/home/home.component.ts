import { Component } from '@angular/core';
import { FooterComponent } from '../../components/footer/footer.component'; // Asegúrate de importar el FooterComponent

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FooterComponent], 
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

}
