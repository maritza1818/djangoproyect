export class Project{
    id: number;
    title: string;
    description: string;
    created_at: string;
    datecompleted: string | null;
    important: boolean;
    discoteca: {
      id: number;
      nombre: string;
    };
    user: {
      id: number;
      username: string;
    };
  
    constructor(
      id: number,
      title: string,
      description: string,
      created_at: string,
      datecompleted: string | null,
      important: boolean,
      discoteca: { id: number; nombre: string },
      user: { id: number; username: string }
    ) {
      this.id = id;
      this.title = title;
      this.description = description;
      this.created_at = created_at;
      this.datecompleted = datecompleted;
      this.important = important;
      this.discoteca = discoteca;
      this.user = user;
    }
  }
  