import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { catchError, Observable, of } from 'rxjs';
import { ErrorDialogComponent } from 'src/app/shared/components/error-dialog/error-dialog.component';
import { Course } from '../../interfaces/course';
import { CoursesService } from '../../services/courses.service';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.scss']
})
export class CoursesComponent implements OnInit {

  // observables de curses[] e apenas Curse[]
  // public coursees: Course[] = [];    // teste* apenas Curse[]
  public courses$: Observable<Course[]>;    // observable de Curse[]

  /*
    // array de colunas para mostrar no mat...
    public displayedColumns = [/*'_id',/ 'name', 'category', 'duration', 'actions'];
  */

  // coursesService: CoursesService;  // outra forma de inicializar fora do construtor da classe

  constructor(
    private coursesService: CoursesService,
    public dialog: MatDialog,
    private router: Router,
    private route: ActivatedRoute
  ) {
    // this.coursesService;   // forma de inicializar fora do parâmetro do construtor da classe
    // this.coursesService = new CoursesService();   // inicializando fora do parâmetro do construtor

    this.courses$ = this.coursesService.list().pipe(
      catchError(error => {
        // console.log(error)
        this.onError("Erro ao carregar Cursos Disponíveis!\n Contate o Support!")
        return of([]);
      })
    );
  }

  onError(ErrorMsg: string) {
    this.dialog.open(ErrorDialogComponent, {
      data:
        ErrorMsg
    })
  }

  onAdd() {
    console.log('On Add')
    this.router.navigate(['new'], { relativeTo: this.route })
  }

  ngOnInit(): void { }

}
