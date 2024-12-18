import { Component } from '@angular/core';

@Component({
  selector: 'app-not-found',
  standalone: true, // Especifica que el componente es standalone
  imports: [],
  templateUrl: './not-found.component.html',
  styleUrls: ['./not-found.component.css']  // Corrección de styleUrl a styleUrls
})
export class NotFoundComponent {
}
