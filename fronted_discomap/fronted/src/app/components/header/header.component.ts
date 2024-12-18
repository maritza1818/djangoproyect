import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterModule } from '@angular/router';  // Importa RouterModule
import { AuthService } from '../../auth.service';  // Asegúrate de importar AuthService

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, RouterModule],  // Asegúrate de importar RouterModule aquí
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  constructor(public router: Router, public authService: AuthService) {}  // Inyecta el AuthService

  logout() {
    this.authService.logout();
    this.router.navigate(['/login']);
  }
}
