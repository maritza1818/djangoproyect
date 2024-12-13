import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { DiscotecaListComponent } from './pages/discoteca-list/discoteca-list.component';
import { TasksListComponent } from './pages/tasks-list/tasks-list.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [RouterModule, TasksListComponent, DiscotecaListComponent],  // Asegúrate de incluir ambos componentes en imports
})
export class AppComponent {
  constructor(private router: Router) {}

  goToTasks() {
    this.router.navigate(['/tasks']);  // Navegar a la ruta de tareas
  }

  goToDiscotecas() {
    this.router.navigate(['/discotecas']);  // Navegar a la lista de discotecas
  }
}
