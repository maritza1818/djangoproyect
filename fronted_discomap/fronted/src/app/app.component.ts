// app.component.ts
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { TasksListComponent } from './tasks-list/tasks-list.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [TasksListComponent],
})
export class AppComponent {
  constructor(private router: Router) {}

  goToTasks() {
    this.router.navigate(['/tasks']);
  }
}
