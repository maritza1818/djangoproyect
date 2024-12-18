import { Routes } from '@angular/router';

// Importar componentes de páginas
import { AuthRedirectComponent } from './auth-redirect/auth-redirect.component';
import { DiscotecaDetailsComponent } from './pages/discoteca-details/discoteca-details.component';
import { DiscotecaListComponent } from './pages/discoteca-list/discoteca-list.component';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { RegisterComponent } from './pages/register/register.component';
import { TasksListComponent } from './pages/tasks-list/tasks-list.component';
import { UserProfileComponent } from './pages/user-profile/user-profile.component';  // Asegúrate de importar el componente de perfil de usuario

export const routes: Routes = [
  { path: '', component: HomeComponent }, // Página principal
  { path: 'discotecas', component: DiscotecaListComponent }, // Lista de discotecas
  { path: 'discotecas/:id', component: DiscotecaDetailsComponent }, // Detalles de una discoteca específica
  { path: 'tasks', component: TasksListComponent }, // Tareas (ejemplo)
  { path: 'login', component: LoginComponent }, // Login de usuario
  { path: 'register', component: RegisterComponent }, // Registro de usuario
  { path: 'profile', component: UserProfileComponent }, // Perfil de usuario
  { path: 'auth-redirect', component: AuthRedirectComponent }, // Redirección después de autenticación
  { path: '**', component: NotFoundComponent } // Página 404 para rutas no existentes
];
