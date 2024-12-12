import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//import { AboutComponent } from './about/about.component';
//import { ContactComponent } from './contact/contact.component';
//import { DiscotecasComponent } from './discotecas/discotecas.component';
import { HomeComponent } from './pages/home/home.component'; // Importar el componente
import { TasksListComponent } from './pages/tasks-list/tasks-list.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },  // Página principal
  { path: 'tasks', component: TasksListComponent },
//{ path: 'discotecas', component: DiscotecasComponent },
 // { path: 'about', component: AboutComponent },
//  { path: 'contact', component: ContactComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
