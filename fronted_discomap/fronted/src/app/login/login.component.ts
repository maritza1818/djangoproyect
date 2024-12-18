import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import { Observer } from 'rxjs';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    console.log('Datos enviados:', { username: this.username, password: this.password });

    const loginObserver: Observer<any> = {
      next: (response) => {
        localStorage.setItem('token', response.token);  // Guarda el token en el almacenamiento local
        this.router.navigate(['/']);  // Redirige a la página principal
      },
      error: (error) => {
        console.error('Error al iniciar sesión:', error);
        alert('Credenciales inválidas. Por favor, inténtalo de nuevo.');
      },
      complete: () => {
        console.log('Inicio de sesión completo');
      }
    };

    this.authService.login(this.username, this.password).subscribe(loginObserver);
  }
}
