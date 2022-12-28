import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { NonNullableFormBuilder } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute } from '@angular/router';
import { ErrorDialogComponent } from 'src/app/shared/components/error-dialog/error-dialog.component';
import { Course } from '../../interfaces/course';
import { CoursesService } from '../../services/courses.service';

@Component({
  selector: 'app-course-form',
  templateUrl: './course-form.component.html',
  styleUrls: ['./course-form.component.scss']
})
export class CourseFormComponent implements OnInit {

  public form = this.formBiulder.group<Course>({
    _id: '',
    name: '',
    category: '',
    duration: ''
  });

  constructor(
    private formBiulder: NonNullableFormBuilder,
    private service: CoursesService,
    private dialog: MatDialog,
    private _snackBar: MatSnackBar,
    private location: Location,
    private route: ActivatedRoute,
  ) {
  }

  onSubmit() {
    this.service.save(this.form.value).subscribe(
      result => { console.log(result); this.onSave() },
      error => { console.error(error); this.onError() }
    );

  }

  onCancel(): void {
    this.location.back();
    console.log("cancel")
  };

  onSave( ) {
    this._snackBar.open("Sucesso ao salvar curso", "close",{
      duration:5000,
      panelClass: "snackbar",

    });
    this.onCancel();
  }
  // console.log("SuccesMsg")

  onError() {
    this.dialog.open(ErrorDialogComponent, {
      data: "Erro ao salvar Curso!\n verifique a conexão com a internet",
    })
    // console.log("MsgError")
  }


  ngOnInit(): void {
    const course: Course = this.route.snapshot.data['course']
    this.form.setValue(
      {
        _id: course._id,
        name: course.name ,
        category: course.category,
        duration: course.duration,
      }

    )
    console.log(this.form.value.duration)
  };

}
