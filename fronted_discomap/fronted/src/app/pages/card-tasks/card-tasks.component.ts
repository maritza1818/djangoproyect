import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Project } from '../../models/projects.model';

@Component({
  selector: 'app-card-tasks',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './card-tasks.component.html',
  styleUrls: ['./card-tasks.component.css']
})
export class CardTasksComponent implements OnChanges {
  @Input() task!: Project;

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['task']) {
      console.log('Datos recibidos en el componente:', this.task);
    }
  }
}

