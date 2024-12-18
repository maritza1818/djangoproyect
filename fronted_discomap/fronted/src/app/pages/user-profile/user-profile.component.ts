import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';  // Importa FormsModule
import { Observable } from 'rxjs';
import { UserService } from '../../user.service';
import { UserProfile } from '../../models/user-profile.model';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  imports: [CommonModule, FormsModule],  // Asegúrate de importar FormsModule aquí
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
  userProfile$: Observable<UserProfile>;
  userId: number = 1;  // Cambia esto para obtener el ID del usuario autenticado
  isEditMode: boolean = false;  // Variable para controlar el modo de edición

  constructor(private userService: UserService) {
    this.userProfile$ = new Observable<UserProfile>();
  }

  ngOnInit(): void {
    this.userProfile$ = this.userService.getUserProfile(this.userId);
    
    // Suscribirse al observable para verificar los datos
    this.userProfile$.subscribe({
      next: (profile) => console.log('UserProfile:', profile),
      error: (err) => console.error('Error loading user profile:', err)
    });
  }

  enableEditMode(): void {
    this.isEditMode = true;
  }

  disableEditMode(): void {
    this.isEditMode = false;
  }

  updateUserProfile(profileData: UserProfile): void {
    this.userProfile$ = this.userService.updateUserProfile(this.userId, profileData).pipe(
      switchMap(() => this.userService.getUserProfile(this.userId))
    );
    this.disableEditMode();
  }
}
