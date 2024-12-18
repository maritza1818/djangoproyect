import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { HeaderComponent } from './components/header/header.component';  
import { DiscotecaListComponent } from './pages/discoteca-list/discoteca-list.component';
import { TasksListComponent } from './pages/tasks-list/tasks-list.component';
import { FooterComponent } from './components/footer/footer.component';  
import { SearchBarComponent } from './components/search-bar/search-bar.component';  // Importa SearchBarComponent

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [RouterModule, TasksListComponent, DiscotecaListComponent, HeaderComponent, FooterComponent, SearchBarComponent],  // Añade SearchBarComponent aquí
})
export class AppComponent {
  constructor(private router: Router) {}

  goToTasks() {
    this.router.navigate(['/tasks']);
  }

  goToDiscotecas() {
    this.router.navigate(['/discotecas']);
  }
}
