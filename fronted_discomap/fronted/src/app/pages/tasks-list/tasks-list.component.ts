import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CardTasksComponent } from '../../pages/card-tasks/card-tasks.component';
import { TasksService } from '../../core/services/tasks.service';
import { Project } from '../../models/projects.model';
import { of } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

@Component({
  selector: 'app-tasks-list',
  templateUrl: './tasks-list.component.html',
  styleUrls: ['./tasks-list.component.css'],
  standalone: true,
  imports: [
    CommonModule,
    CardTasksComponent
  ]
})
export class TasksListComponent implements OnInit {
  tasks: Project[] = [];

  constructor(private tasksService: TasksService) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks(): void {
    this.tasksService.getTasks().pipe(
      map(data => {
        console.log('Datos recibidos de la API:', data); // Verificar aquí
        return data;
      }),
      catchError(error => {
        console.error('Error al obtener las tareas', error);
        return of([]);
      })
    ).subscribe(data => {
      this.tasks = data;
      console.log('Tareas asignadas:', this.tasks); // Verificar aquí
    });
  }
}
