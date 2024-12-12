import { CommonModule } from '@angular/common'; // Para usar ngIf, ngFor, etc.
import { HttpClientModule } from '@angular/common/http'; // Importa HttpClientModule
import { Component, OnInit } from '@angular/core';
import { TasksService } from '../core/services/tasks.service'; // Asegúrate de importar tu servicio



@Component({
  selector: 'app-tasks-list',
  templateUrl: './tasks-list.component.html',
  styleUrls: ['./tasks-list.component.css'],
  standalone: true,  // Hacemos el componente standalone
  imports: [HttpClientModule, CommonModule]  // Importamos HttpClientModule y CommonModule
})
export class TasksListComponent implements OnInit {

  tasks: any[] = [];  // Array donde almacenamos las tareas

  constructor(private tasksService: TasksService) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks(): void {
    this.tasksService.getTasks().subscribe(
      (data) => {
        console.log('Tareas obtenidas:', data);  // Verifica los datos que llegan
        this.tasks = data.tasks;
      },
      (error) => {
        console.error('Error al obtener las tareas', error);
      }
    );
  }
}
