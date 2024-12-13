import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { TasksListComponent } from './pages/tasks-list/tasks-list.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [RouterModule, TasksListComponent],  // Asegúrate de incluir RouterModule en los imports
})
export class AppComponent {
  constructor(private router: Router) {}  // Inyección del Router

  goToTasks() {
    this.router.navigate(['/tasks']);  // Navegar a la ruta de tareas
  }
}
