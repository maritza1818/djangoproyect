import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    console.log('Datos enviados:', { username: this.username, password: this.password });

    this.authService.register(this.username, this.password).subscribe(
      (response: any) => {
        alert('Registro exitoso. Ahora puede iniciar sesión.');
        this.router.navigate(['/login']);  // Redirige al login después del registro
      },
      (error: any) => {
        console.error('Error al registrar:', error);
        alert('Error al registrar. Por favor, inténtelo de nuevo.');
      }
    );
  }
}
